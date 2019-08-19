import sys

from printer.printer import Printer


if len(sys.argv) < 2:
    print('Missing argument. Please provide a message...')
    sys.exit(1)
for msg in sys.argv[1:]:
    p = Printer(msg)
    p.print()
sys.exit(0)
