class Node():
    def __init__(self, val):
        '''
        Node of Linked List
        val  = Value for node
        next = Address of next node linked with current node
        '''
        self.val = val
        self.next = None
        self.prev = None


class Deque():
    def __init__(self):
        '''
        Queue First In First Out (FIFO)
        head   = Linked list starting node
        tail   = Linked list ending node
        length = Current length of Stack
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def l_push(self, val):
        '''
        Push value in Queue
        val = Value push in Queue
        '''
        new_node = Node(val)
        if self.length:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def r_push(self, val):
        '''
        Push value in Queue
        val = Value push in Queue
        '''
        new_node = Node(val)
        if self.length:
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def l_pop(self):
        '''
        Pop up(Return & remove) the bottom value of Queue
        Bottom value means first pushed value in Queue
        '''
        if self.length:
            val, temp = self.head.val, self.head.next
            del self.head
            self.head = temp
            if self.head:
                self.head.prev = None
            self.length -= 1
            return val
        return "Queue is empty!"

    def r_pop(self):
        '''
        Pop up(Return & remove) the bottom value of Queue
        Bottom value means first pushed value in Queue
        '''
        if self.length:
            val, temp = self.tail.val, self.tail.prev
            del self.tail
            self.tail = temp
            if self.tail:
                self.tail.next = None
            self.length -= 1
            return val
        return "Queue is empty!"

    def __len__(self):
        '''
        Magic function to print Queue length using len function

        Example:
            var = Queue()
            print(len(var))
        '''
        return self.length
