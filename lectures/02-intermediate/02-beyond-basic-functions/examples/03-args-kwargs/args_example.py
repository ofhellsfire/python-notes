def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


start = 2

print(hypervolume(start, 1, 2, 3, 4, 5, 6, 7, 8))
