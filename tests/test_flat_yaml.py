from pathlib import Path

from gendiff import generate_diff, parse_files


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_flat_yaml_default():
    path1 = get_test_data_path("file1.yaml")
    path2 = get_test_data_path("file2.yaml")
    file_objects = parse_files(path1, path2)
    actual = generate_diff(file_objects[0], file_objects[1])
    expected = read_file("result.txt")

    assert actual == expected


def test_flat_yml_default():
    path1 = get_test_data_path("file1.yml")
    path2 = get_test_data_path("file2.yml")
    file_objects = parse_files(path1, path2)
    actual = generate_diff(file_objects[0], file_objects[1])
    expected = read_file("result.txt")

    assert actual == expected

