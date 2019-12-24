# Demonstrates 3 cases for exceptions raised in the context manager body


class Baz:

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('inside exit')  # No return, means 'None' is returned


with Baz() as bz:
    print('inside with block')
    raise Exception('some exception')  # must propagate exception


class Foo:
    
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('inside exit')
        return False


with Foo() as f:
    print('inisde with block')
    raise Exception('some exception')  # must propagate exception


class Bar:
    
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('inside exit')
        return True


with Bar() as b:
    print('inisde with block')
    raise Exception('some exception')  # must swallow exception
