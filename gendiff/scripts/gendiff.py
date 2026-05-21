import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file', nargs='*')
    parser.add_argument('second_file', nargs='*')
    args = parser.parse_args()
    parser.print_help()
    return args

def main():
    args = parse_arguments()

if __name__ == "__main__":
    main()