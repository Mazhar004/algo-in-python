class Node:
    def __init__(self, val=None):
        '''
        Node of Linked List
        val  = Value for node
        next = Address of next node linked with current node
        '''
        self.val = val
        self.next = None


class CircularQueue:
    def __init__(self):
        '''
        Circular Queue First In First Out (FIFO)
        head   = Linked list starting node
        tail   = Linked list ending node
        length = Current length of Circular Queue
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, val):
        '''
        Push value in Circular Queue
        val = Value push in Circular Queue
        '''
        node = Node(val)
        if self.head:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        '''
        Pop up(Return & remove) the bottom value of Circular Queue
        Bottom value means first pushed value in Circular Queue
        '''
        if self.length:
            val, temp = self.head.val, self.head.next
            del self.head
            self.head = temp
            self.tail.next = self.head
            if self.head == self.tail:
                self.head.next = None
                self.tail.next = None
            self.length -= 1
            return val
        return ("Circular Queue is empty")

    def __len__(self):
        '''
        Magic function to print Queue length using len function

        Example:
            var = Queue()
            print(len(var))
        '''
        return self.length
