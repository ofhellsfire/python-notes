"""
Example showing reference cycles
"""

import ctypes
import gc


# ctypes module to access unreachable objects by memory address
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]

gc.set_debug(gc.DEBUG_SAVEALL)
gc.disable()  # disable generational gc

lst = []
lst.append(lst)

lst_address = id(lst)

del lst

object_1 = {}
object_2 = {}
object_1["obj2"] = object_2
object_2["obj1"] = object_1

obj_1_address = id(object_1)
obj_2_address = id(object_2)

del object_1, object_2

# uncomment to manuallty run garbage collection
gc.collect()

print("ref count for lst_address:", PyObject.from_address(lst_address).refcnt)
print("ref count for obj_1_address:", PyObject.from_address(obj_1_address).refcnt)
print("ref count for obj_2_address:", PyObject.from_address(obj_2_address).refcnt)

# show what was collected
for item in gc.garbage:
    print(item)
