"""
Example shows surprise, that the `else` block will run immediately if we loop over an empty sequence.
"""

if __name__ == "__main__":

    # for loop
    for i in ():
        print('inside for block')
    else:
        print('inside for-else block')

    # while loop
    while 1 <= 0:
        print('inside while block')
    else:
        print('inside while-else block')