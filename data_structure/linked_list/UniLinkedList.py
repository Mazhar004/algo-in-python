class Node():
    def __init__(self, val=None):
        '''
        Node for Unidirectional Linked List
        value        = Value for node 
        '''
        self.val = val
        self.next_address = None


class UniLinkedList():
    def __init__(self):
        '''
        Unidirectional Linked List
        head = Linked list starting node (head)
        '''
        self.head = None

    def append(self, val):
        '''
        Append value in Linked List
        val = Value append in linked list at last position
        '''
        new_node = Node(val)
        if self.head:
            temp = self.head
            while temp.next_address:
                temp = temp.next_address
            temp.next_address = new_node
        else:
            self.head = new_node

    def delete(self, val):
        '''
        Delete value from Linked List
        val = Find matching value in linked list to delete
        '''
        prev, current = None, self.head
        while current:
            if current.val == val:
                break
            prev, current = current, current.next_address

        if current:
            if current == self.head:
                self.head = self.head.next_address
            else:
                prev.next_address = current.next_address
            print('Value deleted\n')
        else:
            print("Value not found in the list!")
        self.traverse()

    def traverse(self):
        '''
        Print all value of the Linked List
        '''
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next_address
        print("\n")