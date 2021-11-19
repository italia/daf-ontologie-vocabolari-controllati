#!/usr/bin/env python
import json
import logging
from io import BytesIO
from pathlib import Path

import click
import yaml
from deepdiff import DeepDiff
from rdflib import Graph

log = logging.getLogger(__name__)
MIME_JSONLD = "application/ld+json"
MIME_TURTLE = "text/turtle"


def is_recent_than(spath, dpath):
    if not dpath.exists():
        return True

    return dpath.stat().st_mtime <= spath.stat().st_mtime


def parse_graph(vpath_ttl, format=MIME_TURTLE):
    log.info(f"Parsing file: {vpath_ttl}")
    g = Graph()
    g.parse(vpath_ttl, format=format)
    log.warning(f"Parsed file: {vpath_ttl}")
    return g


def yaml_load(fpath):
    return yaml.safe_load(Path(fpath).read_text())


def yaml_to_json(s: str):
    return json.dumps(yaml.safe_load(s), indent=2)


def build_semantic_asset(asset_path: Path, dest_dir: Path = Path(".")):
    log.warning(f"Building {asset_path} in {dest_dir}")

    if "out" in asset_path.suffixes:
        return

    g = parse_graph(asset_path.as_posix())

    for fmt, ext in [("xml", ".rdf"), (MIME_JSONLD, ".jsonld"), ("ntriples", ".nt")]:
        dpath = (dest_dir / asset_path).with_suffix(ext)
        dpath.parent.mkdir(exist_ok=True, parents=True)
        if False and not is_recent_than(asset_path, dpath):
            continue
        ctx = dict(g.namespaces())
        g.serialize(format=fmt, destination=dpath.as_posix(), context=ctx)

        if ext == ".jsonld":
            from pyld import jsonld

            log.warning(f"Normalizing {dpath}")
            indata = yaml.safe_load(dpath.read_text())
            ctx = indata["@context"]
            if "" in ctx:
                del ctx[""]
            json_data = jsonld.compact(indata, ctx)
            dpath.write_text(normalize_json(json_data))


def json_deep_copy(json_data):
    return json.loads(json.dumps(json_data))


def normalize_json(json_data):
    json_data = json_deep_copy(json_data)
    as_list = False
    if isinstance(json_data, list):
        graph = json_data
        as_list = True
        json_data = {}
    else:
        graph = json_data["@graph"]

    json_data["@graph"] = list(sorted(graph, key=lambda x: next(iter(x.values()))))
    #  data["@context"] = list(sorted(data["@context"], key=lambda x: x.keys()))
    return json.dumps(
        json_data["@graph"] if as_list else json_data,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    )


def normalize_json_file(fpath):
    data = json.loads(Path(fpath).read_text())
    json_text = normalize_json(data)
    if DeepDiff(data, json.loads(json_text), ignore_order=True):
        raise Exception("Normalization failed")
    fpath.write_text(json_text)


def normalize_xml_file(fpath):
    fpath = Path(fpath)
    import lxml.etree as ET

    et = ET.parse(BytesIO(fpath.read_bytes()))
    output = BytesIO()
    et.write_c14n(output)
    fpath.write_bytes(output.getvalue())


@click.command()
@click.argument("src")
@click.option("--normalize-json", is_flag=True, default=False)
@click.option("--normalize-xml", is_flag=True, default=False)
@click.option("--build", is_flag=True)
def main(src, normalize_json, normalize_xml, build):
    fpath = Path(src)

    if normalize_json:
        doit = normalize_json_file
        ext = "*.jsonld"
    elif build:
        doit = build_semantic_asset
        ext = "*.ttl"
    elif normalize_xml:
        doit = normalize_xml_file
        ext = "*.rdf"
    else:
        raise Exception("No action specified")

    if fpath.is_dir():
        for f in fpath.glob(f"**/latest/{ext}"):
            log.warning(f"Processing {f}")
            doit(f)


if __name__ == "__main__":
    main()
