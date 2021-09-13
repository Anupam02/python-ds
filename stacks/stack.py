"""
Stack Data Structure
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def peek(self):
        # it prints top of stack
        if not self.is_empty():
            return self.items[-1]
        return None


    def print_stack(self):
        print(self.items)


# s = Stack()
# print(s.is_empty())
# s.push("A")
# s.push("B")
# s.print_stack()
# s.push("C")
# s.print_stack()
# s.pop()
# print(s.is_empty())
# s.print_stack()
# print(s.peek())
