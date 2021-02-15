import argparse
import csv
from pathlib import Path


def read_csv(src_file, output_file):
    with open(src_file) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)
        if output_file:
            f = open(output_file, "w")
            for row in reader:
                f.write(str(row))
        else:
            for row in reader:
                print(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your app.')
    parser.add_argument('inDir', type=Path,
                        help='Path to the file to be read from.')
    parser.add_argument('-d', '--destination', type=Path,
                        help='The name of the file to store the read file in')

    args = parser.parse_args()

    result = read_csv(args.inDir, args.destination)
    print("You have written from: "+str(args.inDir) +
          " to file: "+str(args.destination))
