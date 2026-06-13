import argparse
from pathlib import Path

from gendiff import generate_diff, parse_files


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", 
        help="set format of output", default="plain"
        )
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    path1 = Path(args.first_file)
    path2 = Path(args.second_file)
    file_objects = parse_files(path1, path2)
    diff = generate_diff(file_objects[0], file_objects[1])
    print(diff)


if __name__ == "__main__":
    main()
    
    
