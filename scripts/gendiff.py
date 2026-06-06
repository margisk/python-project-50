import argparse
from gendiff import generate_diff
import json
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output", default="plain")
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    path1 = Path(args.first_file)
    path2 = Path(args.second_file)
    with open(path1, "r") as file1:
        obj1 = json.load(file1)
    with open(path2, "r") as file2:
        obj2 = json.load(file2)

    diff = generate_diff(obj1, obj2)
    print(diff)

if __name__ == "__main__":
    main()
    
    
