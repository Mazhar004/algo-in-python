class Node():
    def __init__(self, val=None, next_address=None):
        '''
        Node for Unidirectional Linked List
        value        = Value for node 
        next_address = Next node address
        '''
        self.val = val
        self.next_address = next_address


class LinkedList():
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
        prev, current = self.head, self.head
        flag = 0
        while current:
            if current.val == val:
                flag = 1
                break
            prev, current = current, current.next_address

        if current:
            if current == self.head:
                self.head = self.head.next_address
            else:
                prev.next_address = current.next_address

        if flag:
            print('Value deleted\n')
        else:
            print("Value not found in the list!")
        print(self)

    def __str__(self):
        '''
        Print all value of the Linked List
        '''
        data = ""
        temp = self.head
        while temp:
            data += str(temp.val)+" "
            temp = temp.next_address
        return data
