from .cfg import rcfg, wcfg
from .utils import ivnd
from typing import Any


def merge_dict(dict1, dict2):
    for key, val in dict1.items():
        if isinstance(val, dict):
            if key in dict2 and type(dict2[key] == dict):
                merge_dict(dict1[key], dict2[key])
        elif key in dict2:
            dict1[key] = dict2[key]

    for key, val in dict2.items():
        if not key in dict1:
            dict1[key] = val

    return dict1


def main(fmt: str, op: str, override: dict[str, Any] = {}):
    cfg = rcfg("dev/vars.yml")["build"]
    wcfg(op, merge_dict(merge_dict(cfg["base"], cfg[fmt]), override))
