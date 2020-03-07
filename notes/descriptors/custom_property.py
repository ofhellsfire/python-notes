class CustomProperty:

    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        if instance is None:
            return self
        elif self.fget is None:
            raise AttributeError('Not existing attribute')
        else:
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('Cannot set attribute')
        else:
            self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('Cannot delete attribute')
        else:
            self.fdel(instance)

    def getter(self, fget):
        print('inside getter')
        return type(self)(fget, self.fset, self.fdel)

    def setter(self, fset):
        print('inside setter')
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        print('inside deleter')
        return type(self)(self.fget, self.fset, fdel)


class Foo:

    bar = CustomProperty()

    def __init__(self, bar, baz):
        self._bar = bar
        self._baz = baz

    @bar.getter
    def bar(self):
        print('inside bar getter')
        return self._bar

    @bar.setter
    def bar(self, value):
        print('inside bar setter')
        self._bar = value

    @bar.deleter
    def bar(self):
        print('inside bar deleter')
        del self._bar

    def _getbaz(self):
        print('inside getbaz property')
        return self._baz

    def _setbaz(self, value):
        print('inside setbaz property')
        self._baz = value

    def _delbaz(self):
        print('inside delbaz property')
        del self._baz

    baz = CustomProperty(fget=_getbaz, fset=_setbaz, fdel=_delbaz)


if __name__ == '__main__':
    foo = Foo(100, 'abcdef')
    print('-----')
    print(foo.bar)
    foo.bar = 500
    print(foo.bar)
    del foo.bar
    print('-----')
    print(foo.baz)
    foo.baz = 'uvwxyz'
    print(foo.baz)
    del foo.baz
