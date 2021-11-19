#!/usr/bin/env python
#
# Validate the repository layout.
from pathlib import Path

import yaml


def test_ndc_config():
    """
    Check that the ndc.config file exists.
    """
    ndc_config = Path("ndc-config.yaml")
    assert ndc_config.is_file(), "ndc.config file not found"

    config = yaml.safe_load(ndc_config.read_text())

    assets = config.get(
        "assets",
        {
            "vocabularies": {"path": "vocabularies"},
            "ontologies": {"path": "ontologies"},
            "schemas": {"path": "schemas"},
        },
    )

    for asset_type in ("vocabularies", "ontologies", "schemas"):
        asset_path = assets.get(asset_type, {}).get("path")
        if not asset_path:
            continue
        if not Path(asset_path).is_dir():
            raise Exception(f"{asset_type} path not found: {asset_path}")


if __name__ == "__main__":
    test_ndc_config()
