# Class Decorator Example

class RemoteLogPusher:

    destination = '192.168.100.15'

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        self.push_msg(self.f.__name__, *args, **kwargs)
        return self.f(*args, **kwargs)

    def push_msg(self, foo, *args, **kwargs):
        print('Pushing message to {dest} from: "{name}"" called with args: "{args}" and kwargs: "{kwargs}"'.format(dest=RemoteLogPusher.destination, name=foo, args=args, kwargs=kwargs))

@RemoteLogPusher
def hello(*args):
    for i in args:
        print('Hello, {}'.format(i))

hello('lena', 'tanya', 'grisha', 'natasha')


# Class Decorator Parameterized Example

class RemoteLogPusher:

    def __init__(self, destination):
        self.destination = destination

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            self.push_msg(f.__name__, *args, **kwargs)
            return f(*args, **kwargs)
        return wrapped

    def push_msg(self, foo, *args, **kwargs):
        print('Pushing message to {dest} from: "{name}" called with args: "{args}" and kwargs: "{kwargs}"'.format(dest=self.destination, name=foo, args=args, kwargs=kwargs))

@RemoteLogPusher('192.168.134.15')
def p_hello(*args):
    for i in args:
        print('Hello, {}'.format(i))

p_hello('anya', 'tanya', 'vova')


# Instance Decorator Example

class RemoteLogPusher:

    def __init__(self, destination, enabled=True):
        self.destination = destination
        self.enabled = enabled

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                self.push_msg(f.__name__, *args, **kwargs)
            return f(*args, **kwargs)
        return wrap

    def push_msg(self, foo, *args, **kwargs):
        print('Pushing message to {dest} from: "{name}"" called with args: "{args}" and kwargs: "{kwargs}"'.format(dest=self.destination, name=foo, args=args, kwargs=kwargs))

aws_logger = RemoteLogPusher('aws://aws-logger-ip-address')
heroku_logger = RemoteLogPusher('heroku://heroku-logger-ip-address', enabled=False)

@aws_logger
def hello(name):
    print('Hello, {}'.format(name))

@heroku_logger
def goodbye(name):
    print('Goodbye, {}'.format(name))

hello('Lena')
goodbye('Barak Khuseinovich')


# Instance Decorator Parameterized Example
class RemoteLogPusher:

    def __init__(self, destination, enabled=True):
        self.destination = destination
        self.enabled = enabled

    def __call__(self, flag):
        def outer(f):
            def wrap(*args, **kwargs):
                if self.enabled:
                    self.push_msg(flag, f.__name__, *args, **kwargs)
                return f(*args,**kwargs)
            return wrap
        return outer

    def push_msg(self, flag, foo, *args, **kwargs):
        print('Flag: {flag}! Pushing message to {dest} from: "{name}"" called with args: "{args}" and kwargs: "{kwargs}"'.format(dest=self.destination, name=foo, args=args, kwargs=kwargs, flag=flag))

aws_logger = RemoteLogPusher('aws://aws-logger-ip-address')

@aws_logger(1380)
def hello(name):
    print('Hello, {}'.format(name))

hello('Masha')
