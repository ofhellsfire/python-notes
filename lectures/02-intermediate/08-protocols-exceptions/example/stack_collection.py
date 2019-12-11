# Demonstrates simple collection protocol implementation by Stack example
# NOTE: this is only for demonstration purpose, don't use it in production!


class Stack:

    class _Element:

        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.length = 0
        self.top = None
        self._current = None

    def __contains__(self, item):
        current_element = self.top
        while current_element:
            if item == current_element.value:
                return True
            current_element = current_element.next
        return False

    def __iter__(self):
        self._current = self.top
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        next_value, self._current = self._current.value, self._current.next
        return next_value

    def __len__(self):
        return self.length

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return NotImplemented
        if len(self) != len(other):
            return False
        for this, that in zip(self, other):
            if this != that:
                return False
        return True

    def __ne__(self, other):
        if not isinstance(other, Stack):
            return NotImplemented
        if len(self) != len(other):
            return True
        for this, that in zip(self, other):
            if this == that:
                return False
        return True

    def __gt__(self, other):
        if not isinstance(other, Stack):
            return NotImplemented
        return len(self) > len(other)

    def __lt__(self, other):
        if not isinstance(other, Stack):
            return NotImplemented
        return len(self) < len(other)

    def add(self, item):
        element = Stack._Element(item)
        self.length += 1
        if self.top is None:
            self.top = element
            return
        temp_element = self.top
        self.top = element
        self.top.next = temp_element

    def pop(self):
        if self.top is None:
            raise ValueError('Stack is empty')
        next_item = self.top.value
        self.length -= 1
        if self.top.next is None:
            self.top = None
        else:
            self.top = self.top.next
        return next_item


mystack = Stack()
print(f'Length of stack is = {len(mystack)}')
mystack.add('1a')
mystack.add('2b')
mystack.add('3c')
mystack.add('4d')
mystack.add('5e')
mystack.add('6f')
mystack.add('7g')
mystack.add('8h')
print(f'Length of stack is = {len(mystack)}')

print(f'Check if "3c" in the stack: {"3c" in mystack}')
print(f'Check if "9i" in the stack: {"9i" in mystack}')
print(f'Check if "10j" in the stack: {"10j" not in mystack}')

print('Iterating through the mystack:')
for item in mystack:
    print(item)
print(f'Length of stack is = {len(mystack)}')

print(f'Pop item: {mystack.pop()}')
print(f'Length of stack is = {len(mystack)}')

otherstack = Stack()
otherstack.add('1a')
otherstack.add('2b')
otherstack.add('3d')
otherstack.add('4d')

print(f'Check if mystack == otherstack: {mystack == otherstack}')
print(f'Check if mystack != otherstack: {mystack != otherstack}')

yastack = Stack()
yastack.add('1a')
yastack.add('2b')
yastack.add('3d')
yastack.add('4d')

print(f'Check if yastack == otherstack: {yastack == otherstack}')
print(f'Check if otherstack != yastack: {otherstack != yastack}')

print(f'Check if mystack is greater than otherstack: {mystack > otherstack}')
print(f'Check if mystack is less than yastack: {mystack < yastack}')
print(f'Check if yastack is less than otherstack: {yastack < otherstack}')
