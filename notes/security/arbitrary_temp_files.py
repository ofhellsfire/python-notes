"""
Shows that absolute path in `os.path.join` discards previous input parameters.
"""

import tempfile


def create_tmp_file(user_id):
    tmp_file = tempfile.NamedTemporaryFile(prefix=user_id)
    print(f'Create tmp file at: {tmp_file.name}')
    ...


if __name__ == '__main__':
    # you get request from user to create tmp file (upload user file) to the 
    # /tmp directory with the user id prefix
    user_id = 'roman_b'
    tmp_file = tempfile.NamedTemporaryFile(prefix=user_id)
    print(f'Tmp file created at: {tmp_file.name}')
    hack_id = '/../root/'
    tmp_file = tempfile.NamedTemporaryFile(prefix=hack_id)
    print(f'Tmp file created at: {tmp_file.name}')
