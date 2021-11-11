#!/usr/bin/env python
#
# Validate .ttl files with pyshacl.
#
# Usage: shacl-validator.py <file.ttl>
import logging
from functools import lru_cache
from pathlib import Path
from sys import argv

from pyshacl import validate
from rdflib.graph import Graph

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


MAX_DEPTH = 5
basedir = Path(__file__).parent


@lru_cache(maxsize=100)
def get_shacl_graph(absolute_path: str) -> Graph:
    if not Path(absolute_path).is_absolute():
        raise ValueError(f"{absolute_path} is not an absolute path")
    log.info(f"Loading SHACL graph from {absolute_path}")
    shacl_graph = Graph()
    shacl_graph.parse(absolute_path, format="turtle")
    return shacl_graph


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: shacl-validator.py <file.ttl>")
        exit(1)

    file = Path(argv[1])
    if not file.exists():
        print("File does not exist: {}".format(file))
        exit(1)

    for file in argv[1:]:
        log.info("Validating {}".format(file))
        shacl_graph = None
        rule_file_path = None
        rule_dir = Path(file).parent
        for _ in range(MAX_DEPTH):
            rule_file_candidate = rule_dir / "rules.shacl"
            if rule_file_candidate.exists():
                rule_file_path = rule_file_candidate.absolute().as_posix()
                shacl_graph = get_shacl_graph(rule_file_path)
                log.info(f"Found shacl file: {rule_file_path}")
                break
            if rule_dir == basedir:
                break
            rule_dir = rule_dir.parent
        try:
            is_valid, graph, report_text = validate(file, shacl_graph=shacl_graph)
            log.info(f"Validation result: {is_valid}, {rule_file_path}, {report_text}")
        except Exception as e:
            log.error(f"Error validating {file}: {rule_file_path} {e}")
            raise
