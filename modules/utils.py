import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Reading to/from files/lists.')
    parser.add_argument('source',
                        help='Path to the file to be read from.')
    parser.add_argument('-target', '--targetfile',
                        help='The name of the file to store the read file in')

    args = parser.parse_args()
    print('Source: '+str(args.folder))
    print('Target: '+str(args.target))


def get_file_names(folderpath, output):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    names = os.listdir(folderpath)
    with open(output, "w") as destination:
        for fil in names:
            destination.write(str(fil) + '\n')


def get_all_file_names(path, dest_file):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
        file = open(dest_file, "w")
        for f in files:
            file.write(str(f) + '\n')


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for f in file_names:
        with open(f, 'r') as file_object:
            print(file_object.readline().rstrip())


def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    substring = "@"
    result = [string for string in file_names if substring in string]
    for r in result:
        print(r)


def write_headlines(md_files, out):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    for md in md_files:
        with open(md, "r") as fi:
            for ln in fi:
                if ln.startswith("#"):
                    with open(out, "w") as destination:
                        destination.write(str(ln) + '\n')
