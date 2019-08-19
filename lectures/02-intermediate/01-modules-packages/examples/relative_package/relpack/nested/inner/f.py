from . import d
from .e import func_from_e
from ..nested.b import func_from_b


def func_from_f():
    print('func_from_f()')


d.func_from_d()
func_from_e()
func_from_b()
