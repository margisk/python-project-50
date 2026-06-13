import json
from pathlib import Path

import yaml


def json_parser(file):
    with open(file, 'r') as f:
        obj = json.load(f)
        return obj
    

def yaml_parser(file):
    with open(file, 'r') as f:
        obj = yaml.safe_load(f)
        return obj


def parse_file(file: Path):
    if file.suffix == ".json":
        return json_parser(file)
    elif file.suffix == ".yaml" or file.suffix == ".yml":
        return yaml_parser(file)


def parse_files(file1: Path, file2: Path):
    # naming is a bit dumb
    # to fix: file extensions might be different
    obj1 = parse_file(file1)
    obj2 = parse_file(file2)
    return obj1, obj2