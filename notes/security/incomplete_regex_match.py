import re


PATTERN = re.compile(r".*(union)|(select).*")


def is_sql_injection(query):
    if re.match(PATTERN, query):  # re.search(...) will catch examples below though
        return True
    return False


if __name__ == '__main__':
    query_uno = 'select * from table'
    print(f'Is "{query_uno}" sql injection: {is_sql_injection(query_uno)}')
    query_dos = 'ololo \n select * from table'
    print(f'Is "{query_dos}" sql injection: {is_sql_injection(query_dos)}')
