"""
Demonstration of class and metaclass with all the important stuff implemented.
"""

class Meta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(f"Meta.__prepare__(mcs={mcs}, name={name}, bases={bases}, **{kwargs})")
        return {       # we can return just `{}` if we don't want to set class attrs at this point
            "a": 100,  # this sets class attrs before class is created
            "b": 200
        }

    def __new__(mcs, name, bases, attrs, **kwargs):
        print(f"Meta.__new__(mcs={mcs}, name={name}, bases={bases}, attrs=[{','.join(attrs)}], kwargs={{{kwargs}}})")
        return super().__new__(mcs, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs, **kwargs):
        print(f"Meta.__init__(cls={cls}, name={name}, bases={bases}, attrs=[{','.join(attrs)}], **{kwargs})")
        return super().__init__(name, bases, attrs)
    
    def __call__(cls, *args, **kwargs):
        print(f"Meta.__call__(cls={cls}, args={args}, kwargs={kwargs})")
        return super().__call__(*args, **kwargs)


class Class(metaclass=Meta, extra=1):

    def __new__(cls, myarg):
        print(f"Class.__new__(cls={cls}, myarg={myarg})")
        return super().__new__(cls)
    
    def __init__(self, myarg):
        print(f"Class.__init__(self={self}, myarg={myarg})")
        self.myarg = myarg
        return super().__init__()
    
    def __str__(self):
        return f"<instance of Class; myargs={getattr(self, 'myarg', 'MISSING')}>"


if __name__ == "__main__":
    foo = Class(200)
    print(f"{foo.a}")
    print(f"{foo.b}")
