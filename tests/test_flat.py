import gendiff
import json
from pathlib import Path

import pytest

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_flat_json():
    json_obj1 = json.loads(read_file("file1.json"))
    json_obj2 = json.loads(read_file("file2.json"))
    actual = generate_diff(json_obj1, json_obj2)
    expected = read_file("result.txt")

    assert actual == expected

