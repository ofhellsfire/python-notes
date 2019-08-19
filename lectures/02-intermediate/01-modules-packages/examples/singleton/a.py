from printer import printer


def a():
    printer.msg = 'my message'
    printer.rev_print()
    print(printer.time_creation)
