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

    def swap_node(self, key1, key2):
        if key1 == key2:
            return None
        
        curr_node1 = self.head
        key1_node = None
        prev_node1 = None
        next_node1 = None
        while curr_node1 is not None:
            if curr_node1.data == key1:
                key1_node = curr_node1
                break
            prev_node1 = curr_node1
            curr_node1 = curr_node1.next
        
        curr_node2 = self.head
        key2_node = None
        prev_node2 = None
        next_node2 = None
        while curr_node2 is not None:
            if curr_node2.data == key2:
                key2_node = curr_node2
                break
            prev_node2 = curr_node2
            curr_node2 = curr_node2.next

        # check if key1 and key2 are present in linked list
        if not key1_node:
            print(f"{key1} is not present in linked list")
            return None
        if not key2_node:
            print(f"{key2} is not present in the linked list")
            return None
        # now check if prev_node1 is not null 
        # if its null it means key1 is the head
        if not prev_node1:
            # in this case its a head node
            # now make the other node as head node
            print('inside if 1')
            next_node1 = key1_node.next
            next_node2 = key2_node.next

            self.head = key2_node
            key2_node.next = next_node1

            prev_node2.next = key1_node
            key1_node.next = next_node2
        elif not prev_node2:
            # in this case key2 is head node
            print('inside if 2')
            next_node2 = key2_node.next
            next_node1 = key1_node.next

            self.head = key1_node
            key1_node.next = next_node2

            prev_node1.next = key2_node
            key2_node.next = next_node1
        else:
            print('inside else')
            # if none of them are head node
            next_node1 = key1_node.next
            next_node2 = key2_node.next

            prev_node1.next = key2_node
            key2_node.next = next_node1

            prev_node2.next = key1_node
            key1_node.next = next_node2

             

   
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
    llist.swap_node(1, 3)
    llist.print()
    llist.swap_node(3, 2)
    # print(llist.len_iterative())
    # llist.print()

if __name__ == '__main__':
    main()
