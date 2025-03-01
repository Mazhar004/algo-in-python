class Node():
    def __init__(self, val=None):
        '''
        Node for Bidirectional Linked List
        val          = Value of the node
        prev_address = Address of previous node linked with current node
        next_address = Address of next node linked with current node
        '''
        self.val = val
        self.prev_address = None
        self.next_address = None


class BiLinkedList():
    def __init__(self):
        '''
        Biidirectional Linked List
        head = Linked list starting node
        tail = Linked list ending node
        '''
        self.head = None
        self.tail = None

    def append(self, val):
        '''
        Append value in Linked List
        val = Value append in Linked list at last position
        '''
        new_node = Node(val)
        if self.head:
            self.tail.next_address = new_node
            new_node.prev_address = self.tail
        else:
            self.head = new_node
        self.tail = new_node

    def delete(self, val):
        '''
        Delete value from Linked List
        val = Find matching value in Linked list to delete
        '''
        current = self.head

        while current:
            if current.val == val:
                break
            current = current.next_address

        if current:
            if current == self.head:
                self.head = self.head.next_address
                self.head.prev_address = None
            else:
                current.prev_address.next_address = current.next_address
                if current.next_address != None:
                    current.next_address.prev_address = current.prev_address
                else:
                    self.tail = current.prev_address
            del current
            print('Value deleted\n')
        else:
            print("Value not found in the list!")
        self.traverse()

    def traverse(self, reverse=False):
        '''
        Print all value of the Linked List
        reverse = Represent direction of list traversing
        '''
        if reverse:
            temp = self.tail
            while temp:
                print(temp.val, end=" ")
                temp = temp.prev_address
        else:
            temp = self.head
            while temp:
                print(temp.val, end=" ")
                temp = temp.next_address
        print('\n')
