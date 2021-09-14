class Node:
    """
    Node class for a single node.
    it contains data and next pointer.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    """
    Class for LinkedList which uses
    Node class objects
    """
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

    def prepend(self, data) -> None:
        new_node = Node(data)
    
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print('Previous node is not in the list')
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key) -> None:
        """Delete a node which has data as key
           Here we have to look at two edge cases
           if node to delete is head
           else otherwise

        Args:
            key (int/str/bool/etc): [data type]
        """
        curr_node = self.head
        prev_node = None
        node_to_delete = None
        while curr_node is not None:
            node_data = curr_node.data
            if node_data == key:
                node_to_delete = curr_node
                break
            prev_node = curr_node
            curr_node = curr_node.next
        if not node_to_delete:
            print('Sorry data not found')
        else:
            if not prev_node:
                # in this case it would be head node
                self.head = curr_node.next
            else:
                # if its not head node
                prev_node.next = curr_node.next
    
    def delete_node_by_position(self, position):
        count = 0
        curr_node = self.head
        prev_node = None
        node_to_delete = None
        while curr_node is not None:
            if position == count:
                node_to_delete = curr_node
                break
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        if not node_to_delete:
            print(f'Position {position} not found')
        else:
            if not prev_node:
                # its 0 (head)
                self.head = curr_node.next
            else:
                prev_node.next = curr_node.next
   
    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' -> ')
            curr_node = curr_node.next
        print('NULL')

    def len_iterative(self):
        count = 0
        curr_node = self.head
        
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)



def main():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.print()
    llist.append(3)
    llist.append(4)
    llist.print()
    llist.prepend(10)
    llist.print()
    second_node = llist.head.next
    llist.insert_after_node(second_node, 100)
    llist.print()
    llist.delete_node(10)
    llist.print()
    llist.prepend(10)
    llist.print()
    llist.delete_node(100)
    llist.print()
    llist.delete_node_by_position(0)
    llist.print()
    llist.delete_node_by_position(3)
    llist.print()
    llist.delete_node_by_position(4)
    llist.print()
    print(llist.len_iterative())
    print(llist.len_recursive(llist.head))

if __name__ == '__main__':
    main()
