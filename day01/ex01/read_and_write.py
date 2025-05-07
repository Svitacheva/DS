def convert_csv_to_tsv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_file, \
            open(output_file, 'w', encoding='utf-8', newline='') as tsv_file:
        inside_quote = False
        for line in csv_file:
            new_line = []
            for char in line:
                if char == '"':
                    inside_quote = not inside_quote
                if char == ',' and not inside_quote:
                    new_line.append('\t')
                else:
                    new_line.append(char)
            tsv_file.write(''.join(new_line))


if __name__ == '__main__':
    convert_csv_to_tsv('ds.csv', 'ds.tsv')
