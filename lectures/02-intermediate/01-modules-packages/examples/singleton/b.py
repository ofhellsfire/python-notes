from printer import printer


def b():
    printer.msg = 'your message'
    printer.rev_print()
    print(printer.time_creation)
