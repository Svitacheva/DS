import sys


def caesar_cipher(text, shift, mode):
    new_text = []
    for char in text:
        code = ord(char)
        if 97 <= code <= 122:  # lower
            base = 97
            new_code = (code - base + (shift if mode ==
                        'encode' else -shift)) % 26 + base
        elif 65 <= code <= 90:  # upper
            base = 65
            new_code = (code - base + (shift if mode ==
                        'encode' else -shift)) % 26 + base
        elif char in ' ,.:@?!/#$%&-' or 48 <= code <= 57:  # symbols and numbers
            new_code = code
        else:
            print('The script does not support your language yet')
            continue
        new_text.append(chr(new_code))
    print(''.join(new_text))


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Error')
        sys.exit(1)
    mode, text, shift = sys.argv[1], sys.argv[2], int(sys.argv[3])
    if mode not in ('encode', 'decode'):
        print('Error')
        sys.exit(1)
    caesar_cipher(text, shift, mode)
