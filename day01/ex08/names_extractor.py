import sys


def extract_name():
    lines = open_file()
    new_lines = parse_lines(lines)
    create_and_write_in_file(new_lines)


def open_file():
    if len(sys.argv) != 2:
        print('Error')
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path) as file:
        return file.readlines()


def parse_lines(lines):
    new_lines = []
    for line in lines:
        name = line.split('.')[0].capitalize()
        surname = (line.split('.')[1]).split('@')[0].capitalize()
        new_line = f"{name}\t{surname}\t{line}"
        new_lines.append(new_line)
    return new_lines


def create_and_write_in_file(new_lines):
    with open('employees.tsv', 'w') as file:
        first_line = 'Name\tSurname\tE-mail\n'
        file.writelines(first_line)
        file.writelines(new_lines)


if __name__ == '__main__':
    extract_name()
