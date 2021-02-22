from modules.utils import get_all_file_names, get_file_names, print_line_one, print_emails, write_headlines

get_file_names("C:\\Users\\claes\\PycharmProjects\\Giraffe", "file1.txt")

get_all_file_names(
    "C:\\Datamatiker\\4.semester\\Python\\master\\docker_notebooks\\server", "file1.txt")

print_line_one(['C:\\Users\\claes\\PycharmProjects\\Giraffe\\file2.txt', 'C:\\Users\\claes\\PycharmProjects\\Giraffe\\file2.txt',
                'C:\\Users\\claes\\PycharmProjects\\Giraffe\\file2.csv'])

print_emails(['af@lev2.py', 'aflev2B.py', 'arg_parse.py',
              'dictiona@ries4.py', 'dictionar@ies5.py'])
