import sys


def get_begin_letter(email):
    with open('employees.tsv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 3 and parts[2].lower() == email.lower():
                return (
                    f"Dear {parts[0]}, welcome to our team. "
                    f"We are sure that it will be a pleasure to work with you. "
                    f"That's a precondition for the professionals that our company hires."
                )


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error")
    else:
        print(get_begin_letter(sys.argv[1]))
