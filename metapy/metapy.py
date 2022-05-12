import argparse
import json

def read_meta(path_to_file):
    with open(path_to_file, "r") as f:
        meta = json.load(f)

    return meta

def write_meta(meta, path_to_file):
    json_meta = json.dumps(meta, indent = 4)

    with open(path_to_file, "w") as f:
        f.write(json_meta)

def main(args):O
    print("It's alive!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Metadata interaction tool.')
    parser.add_argument('-o',
                        '--output',
                        dest='output',
                        action='store',
                        help='Path to output file.')
    parser.add_argument('-s',
                        '--substitution',
                        dest='subs',
                        action='store',
                        help='Path to JSON file of substitutions.')
    args = parser.parse_args()
    main(args)
