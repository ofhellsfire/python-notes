"""
Example shows unexpected behavior of slices with strides on Unicode decoded strings

To avoid such problems, don't use stride along with start and end indexes. If you 
have to use stride, prefer making it a positive value and omit start and end indexes.
If you have to use stride with start and end indexes, consider using one assigment to
stride and another to slice.
"""

if __name__ == "__main__":
    foo = "this is just a string"
    bar = "это просто какая-то строка"
    bar_encoded = bar.encode("utf-8")

    print(foo)
    print(foo[::-1])

    print(bar_encoded)
    reversed_bar = bar_encoded[::-1]
    print(reversed_bar.decode("utf-8"))  # this throws an exception, because it works only with bytes and ASCII
