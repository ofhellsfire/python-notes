"""
Here are some classes that use steadily increasing priority attribute access 
mechanisms to override the behavior of their parent class.

https://stackoverflow.com/a/14787522

"""

class O1:
    def __getattr__(self, name):
        return f"__getattr__ has the lowest priority to find {name}"


class O2(O1):
    var = "Class variables and non-data descriptors are low priority"
    def method(self): # functions are non-data descriptors
        return self.var


class O3(O2):
    def __init__(self):
        self.var = "instance variables have medium priority"
        self.method = lambda: self.var # doesn't recieve self as arg


class O4(O3):
    @property # this decorator makes this instancevar into a data descriptor
    def var(self):
        return "Data descriptors (such as properties) are high priority"

    @var.setter # let O3's constructor set a value in __dict__
    def var(self, value):
        self.__dict__["var"]  = value # but I know it will be ignored


class O5(O4):
    def __getattribute__(self, name):
        if name in ("magic", "method", "__dict__"): # for a few names
            return super().__getattribute__(name) # use normal access
        return f"__getattribute__ has the highest priority for {name}"


if __name__ == '__main__':
    o1 = O1()
    print(o1.var)

    print('----')

    o2 = O2()
    print(o2.var)
    print(o2.method)
    print(o2.method())

    print('----')

    o3 = O3()
    print(o3.method)
    print(o3.method())
    print(o3.var)

    print('----')

    o4 = O4()
    print(o4.method())
    print(o4.var)
    print(o4.__dict__["var"])

    print('----')

    o5 = O5()
    print(o5.method)
    print(o5.method())
    print(o5.__dict__["var"])
    print(o5.magic)
