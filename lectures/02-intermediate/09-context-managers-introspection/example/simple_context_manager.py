# Demonstrates basic context manager


class LoggingContextManager:

    def __enter__(self):
        print('inside enter')
        return 'inside with-block'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('inside exit')
        else:
            print(f'inside exit: {exc_type} {exc_val} {exc_tb}')
            return


with LoggingContextManager() as x:
    print(x)

with LoggingContextManager() as x:
    raise ValueError('broken')