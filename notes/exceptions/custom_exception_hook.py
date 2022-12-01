import datetime
import sys


def custom_exception_hook(exc_type, exc_value, tb):
    with open('/tmp/python_custom_exception_hook.log', 'a') as f:
        f.write(f'{datetime.datetime.now()}\n')
        f.write('Traceback:\n')
        filename = tb.tb_frame.f_code.co_filename
        name = tb.tb_frame.f_code.co_name
        line_no = tb.tb_lineno
        f.write(f'File {filename} line {line_no}, in {name}\n')
        f.write(f'{exc_type.__name__}, Message: {exc_value}\n')
        f.write(f'\n')


sys.excepthook = custom_exception_hook


def main():
    a = [1, 2, 3]
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])


if __name__ == '__main__':
    main()  # see /tmp/python_custom_exception_hook.log (linux only)
