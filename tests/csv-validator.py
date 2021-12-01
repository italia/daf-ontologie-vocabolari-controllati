#!/usr/bin/env python3
#
# CSV Validator with frictionless
#
import json
import logging
import re
from pathlib import Path
from sys import argv

from frictionless import validate

log = logging.getLogger(__name__)

RE_FIELD = re.compile("^[a-zA-Z0-9_]{3,64}$")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: %s [file1.csv file2.csv]" % argv[0])
        exit(1)

    errors = {}

    for f in argv[1:]:
        current_errors = None
        fpath = Path(f)
        log.info(f"Validating {fpath}")
        if not fpath.is_file():
            print("File not found: %s" % fpath)
            exit(1)

        report = validate(fpath)

        if not report.valid:
            current_errors = errors[fpath.as_posix()] = report.flatten(
                ["rowPosition", "fieldPosition", "code"]
            )
            log.error(f"Invalid file: {fpath}.")
            log.debug(json.dumps(current_errors, indent=2))
            continue

        for field_name in [
            field.name
            for tasks in report.tasks
            for field in tasks.resource.schema.fields
        ]:
            if not RE_FIELD.match(str(field_name)):
                log.error(f"Invalid field name: {field_name}")
                errors[fpath.as_posix()] = [f"Invalid field name: {field_name}"]
                continue

        log.info(f"File {fpath} is valid")
    if errors:
        log.debug("Found errors: line, field, error\n" + json.dumps(errors, indent=2))
        log.error(f"Validation failed for {fpath.as_posix()}.")
        exit(1)

    log.info("All files are valid")
    exit(0)
