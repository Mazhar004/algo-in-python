class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack():
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if self.length:
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.length:
            val, temp = self.head.val, self.head.next
            del self.head
            self.head = temp
            self.length -= 1
            return val
        return "Stack is empty!"

    def peek(self):
        if self.length:
            return self.head.val
        return "Stack is empty!"

    def __len__(self):
        return self.length
