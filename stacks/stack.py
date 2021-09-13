"""
Stack Data Structure
"""


class Stack():
    """
    Stack Class for Stack Data Structure.

    Last In , First Out ( LIFO )

    Supports three constant following operations
    push(x) - insert x into the stack
    pop(x) - removes the newest element
    top(x) - returns the top of stack or newest element
    is_empty(x) - checks if stack is empty or not
    """
    def __init__(self):
        """
        Constructor for Stack by using empty list.
        """
        self.items = []

    def push(self, item):
        """Push the item to top of Stack

        Args:
            item (string/int/bool - it can be of any type \
                as python supports dynamic typing): [item to be added]
        """
        self.items.append(item)

    def pop(self):
        """Pop the item from top of stack

        Returns:
            [string/int/bool- can be of any type]: [top element of the stack]
        """
        return self.items.pop()

    def is_empty(self):
        """Check if stack is empty.

        Returns:
            [bool]: [boolean flag whether stack is empty or not]
        """
        is_stack_empty = True
        if len(self.items):
            is_stack_empty = False
        return is_stack_empty

    def top(self):
        """Get the top element of stack

        Returns:
            [string/int/bool - can of any type]: [top element of stack]
        """
        top_elem = None
        if not self.is_empty():
            top_elem = self.items[-1]
        return top_elem
