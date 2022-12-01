# Constants Alternatives Memory Consumption

## `__slots__` attribute

Via pympler

```
                  types |   # objects |      total size
======================= | =========== | ===============
                   type |           1 |       896     B
     __main__.Constants |           1 |        32     B
```

## `@property` decorator

Via pympler

```
                  types |   # objects |      total size
======================= | =========== | ===============
                   type |           1 |         1.04 KB
                   code |           1 |       176     B
               property |           2 |       144     B
         function (DOS) |           1 |       136     B
         function (UNO) |           1 |       136     B
      getset_descriptor |           2 |       128     B
     __main__.Constants |           1 |        48     B
```

## `namedtuple()` factory function

Via pympler

```
                      types |   # objects |   total size
=========================== | =========== | ============
                       type |           1 |    896     B
                       dict |           1 |    600     B
                       cell |           7 |    280     B
                      tuple |           4 |    216     B
           function (_make) |           1 |    136     B
         function (_asdict) |           1 |    136     B
        function (__repr__) |           1 |    136     B
         function (__new__) |           1 |    136     B
  function (__getnewargs__) |           1 |    136     B
        function (_replace) |           1 |    136     B
  _collections._tuplegetter |           2 |     96     B
         __main__.Constants |           1 |     56     B
                classmethod |           1 |     48     B
               staticmethod |           1 |     48     B
```

## `@dataclass` decorator

Via pympler

```
                         types |   # objects |   total size
============================== | =========== | ============
                          type |           1 |      1.04 KB
                          code |           6 |      1.03 KB
                          dict |           3 |    896     B
           function (__repr__) |           2 |    272     B
                           set |           1 |    216     B
                          cell |           4 |    160     B
           function (__init__) |           1 |    136     B
        function (__setattr__) |           1 |    136     B
           function (__hash__) |           1 |    136     B
             function (__eq__) |           1 |    136     B
        function (__delattr__) |           1 |    136     B
             getset_descriptor |           2 |    128     B
  dataclasses._DataclassParams |           1 |     80     B
                         tuple |           1 |     48     B
            __main__.Constants |           1 |     48     B
```

## `__setattr__()` special method

Via pympler

```
                   types |   # objects |      total size
======================== | =========== | ===============
                    type |           1 |         1.04 KB
  function (__setattr__) |           1 |       136     B
       getset_descriptor |           2 |       128     B
      __main__.Constants |           1 |        48     B
```
