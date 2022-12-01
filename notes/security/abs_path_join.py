"""
Shows that absolute path in `os.path.join` discards previous input parameters.
"""

import os


def read_file_from_tmp(filename):
    tmp_path = '/tmp'
    path = os.path.join(tmp_path, filename)
    print(f'Show contents of filename for path: {path}')
    ...


if __name__ == '__main__':
    # you get request from user to show specific file from /tmp
    user_input = 'some_file.txt'
    read_file_from_tmp(user_input)
    hack_input = '/etc/somesecretservice/config.conf'
    read_file_from_tmp(user_input)
