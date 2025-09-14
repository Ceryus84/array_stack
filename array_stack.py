"""
Aidan Butcher
CS 3450 - Algorithms & Data Structures
An in-class demonstration of a Stack class.
"""


class Empty(Exception):
    """Exception for if a stack is empty."""


class ArrayStack():
    """LIFO (Last In First Out) Stack implementation using a Python list as
    underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []  #nonpublic list instance

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._data)

    def __str__(self) -> list:
        """Return the list when printed."""
        return f"Stack: {self._data}"

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e: int):
        """Add element e to the top of the stack."""
        self._data.append(e)  #new item stored at the end of the list

    def top(self) -> int:
        """Return (but not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]  #the last item in the list

    def pop(self) -> int:
        """Remove and return the element at the top of the stack (i.e. LIFO)
        Raise Empty exception if the stack is empty."""

        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()  #remove last item from list


if __name__ == '__main__':
    S = ArrayStack()
    S.pop()
    S.push(3)
    S.push(5)
    print(S)
