class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            head_ptr = self.head
            while head_ptr.next is not None:
                head_ptr = head_ptr.next
            head_ptr.next = new_node
        
    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' -> ')
            curr_node = curr_node.next
        print('NULL')


def main():
    llist = LinkedList()
    llist.append('1')
    llist.append('2')
    llist.print()
    llist.append('3')
    llist.append('4')
    llist.print()


if __name__ == '__main__':
    main()
