# Iterator Protocol Example


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.length = 0
        self.root = None

    def add(self, value):
        node = Node(value)
        self.length += 1
        if not self.root:
            self.root = node
            return
        last_node = self._get_last_node()
        last_node.next = node

    def _get_last_node(self):
        if not self.root:
            return
        node = self.root
        while node.next is not None:
            node = node.next
        return node


class LinkedListIterator:

    def __init__(self, linked_list):
        self.linked_list = linked_list
        self._current = None
        self._endFlag = False

    def __iter__(self):
        return self

    def __next__(self):
        self._set_init_current()
        if self._endFlag is True:
            self._endFlag = False
            raise StopIteration
        next_value = self._current.value
        if self._current.next is None:
            self._endFlag = True
        self._current = self._current.next
        return next_value

    def _set_init_current(self):
        if self.linked_list.root is None:
            raise StopIteration
        elif self._current is None:
            self._current = self.linked_list.root
    

if __name__ == '__main__':
    lst = LinkedList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst.add(5)
    lst.add(8)
    lst.add(9)
    for i in LinkedListIterator(lst):
        print(i)
