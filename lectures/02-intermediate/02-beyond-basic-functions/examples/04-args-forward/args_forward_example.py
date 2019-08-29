def trace(func, *args, **kwargs):
    print(args)
    print(kwargs)
    result = func(*args, **kwargs)
    print(result)
    return result


print(trace(int, "ff", base=16))
