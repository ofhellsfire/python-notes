def foo(pos_arg1, pos_arg2, *args, kwarg1, kwarg2, **kwargs):
    print('pos_arg1 = {}'.format(pos_arg1))
    print('pos_arg2 = {}'.format(pos_arg2))
    print('*args = {}'.format(args))
    print('kwarg1 = {}'.format(kwarg1))
    print('kwarg2 = {}'.format(kwarg2))
    print('**kwargs = {}'.format(kwargs))

foo('uno', 'dos', 'tres', 'cuatro', kwarg1='sinco', kwarg2='seis', kwarg3='siete', kwarg4='ocho')
