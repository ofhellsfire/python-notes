"""
Show example of extended zip slip.

Example of creation suspicious archive:

$ tar -Pcvf hackarchive.tar /tmp/hackfile.txt '../hackfile2.txt'
"""

import os
import sys
import tarfile


def get_upload_from_user(archive_path):
    tf = tarfile.TarFile(archive_path)
    tf.extractall()
    # after this call check /tmp/hackfile.txt '../hackfile2.txt' are extracted
    assert os.path.isfile('/tmp/hackfile.txt')
    assert os.path.isfile('../hackfile2.txt')
    os.remove('/tmp/hackfile.txt')
    os.remove('../hackfile2.txt')


if __name__ == '__main__':
    filepath = sys.argv[1]
    print(filepath)
    get_upload_from_user(filepath)
