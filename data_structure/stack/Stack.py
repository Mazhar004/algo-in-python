class Node():
    def __init__(self, val):
        '''
        Node of Linked List
        val  = Value for node
        next = Address of next node linked with current node
        '''
        self.val = val
        self.next = None


class Stack():
    def __init__(self):
        '''
        Stack Last In First Out (LIFO)
        head   = Linked list starting node
        length = Current length of Stack
        '''
        self.head = None
        self.length = 0

    def push(self, val):
        '''
        Push value in Stack
        val = Value push in Stack
        '''
        new_node = Node(val)
        if self.length:
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        '''
        Pop up(Return & remove) the top value of Stack
        Top value means last pushed value in Stack
        '''
        if self.length:
            val, temp = self.head.val, self.head.next
            del self.head
            self.head = temp
            self.length -= 1
            return val
        return "Stack is empty!"

    def peek(self):
        '''
        Peek up(Only return,not remove) the top value of Stack
        '''
        if self.length:
            return self.head.val
        return "Stack is empty!"

    def __len__(self):
        '''
        Magic function to print Stack length using len function

        Example:
            var = Stack()
            print(len(var))
        '''
        return self.length
