def sum_four(arg1, arg2, arg3, arg4):
    return sum([arg1, arg2, arg3, arg4])


def slow_sum(start, *items):
    result = start
    for item in items:
        result += item
    return result


def swap_keys_values(**kwargs):
    # Note: You can loose data
    return {val: key for key, val in kwargs.items()}


seq1 = range(1, 50)
seq2 = [2, 4, 6, 8]
print(slow_sum(0, *seq1))
print(slow_sum(100, *seq2))

values = (1, 2, 3, 4)
print(sum_four(values[0], values[1], values[2], values[3]))
print(sum_four(*(1, 2, 3, 4)))

d = dict(uno='one', dos='two', tres='three', cuatro='four')
print(swap_keys_values(**d))
