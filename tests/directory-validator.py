#!/usr/bin/env python
#
# Validate .ttl files with pyshacl.
#
# Usage: directory-validator.py <file.ttl>
import difflib
import logging
from distutils.version import LooseVersion
from pathlib import Path
from sys import argv

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)

MAX_DEPTH = 5
basedir = Path(__file__).parent


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: directory-validator.py <file.ttl>")
        exit(1)

    errors = []
    for f in argv[1:]:
        log.info("Validating {}".format(f))

        fpath = Path(f)
        if not fpath.exists():
            print("File does not exist: {}".format(fpath))
            exit(1)

        if fpath.parent.name != "latest":
            continue
        folders = [
            x.name
            for x in fpath.parent.parent.glob("*/")
            if x.name != "latest" and x.is_dir() and x.name[:2] != "v."
        ]
        log.debug("Identified folders: ", folders)
        last_version_dirname = sorted(LooseVersion(x) for x in folders)[-1]
        log.debug("Version:", last_version_dirname)
        cpath = fpath.parent.parent / last_version_dirname.vstring / fpath.name

        if cpath.suffix not in (".ttl", ".jsonld", ".rdf"):
            continue

        with open(cpath) as f_latest, open(fpath) as f_version:
            diffs = []
            diff = difflib.unified_diff(
                f_latest.readlines(),
                f_version.readlines(),
                fromfile=cpath.as_posix(),
                tofile=fpath.as_posix(),
            )
            diffs = "".join(diff)
            if diffs:
                errstr = f"ERROR: files are different: {cpath} {fpath}"
                errors.append(errstr)
                log.error(diffs)
            else:
                print(f"File {cpath} is up to date with {fpath}")

    if errors:
        raise ValueError("Errors found: " + "\n".join(errors))
    else:
        print("No errors found")
