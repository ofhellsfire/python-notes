# Nested Comprehension Example

TABLE_SEPARATOR = '|'
FORMAT = f'{TABLE_SEPARATOR} {{:>2}} '


def get_table_length(table, frmt):
    return len([rows for rows in table]) * len(frmt.format('')) + 1


def print_row_separator(length, sep='-'):
    print(sep * length)


def main():
    mul_table = [[x * y for x in range(1,10)] for y in range(1,10)]
    table_len = get_table_length(mul_table, FORMAT)

    for row in mul_table:
        print_row_separator(table_len)
        for col in row:
            print(FORMAT.format(col), end='')
        print(TABLE_SEPARATOR)
    print_row_separator(table_len)


if __name__ == '__main__':
    main()
