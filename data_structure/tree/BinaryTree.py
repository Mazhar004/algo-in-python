class Node():
    def __init__(self, val=None):
        '''
        Node for Tree
        value        = Value for node
        '''
        self.val = val
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        '''
        Binary Tree
        Root = Linked list starting node (root)
        '''
        self.root = None

    def insert(self, val):
        '''
        Append value in Binary tree
        val = Value append in binary tree
              Value greater or equal to the parent goes to right
              Value smaller to the parent goes to left
        '''
        new_node = Node(val)
        temp = self.root
        if temp:
            while temp:
                parent = temp
                if temp.val <= val:
                    temp, flag = temp.right, 1
                else:
                    temp, flag = temp.left, 0
            if flag:
                parent.right = new_node
            else:
                parent.left = new_node
        else:
            self.root = new_node

    def search(self, val):
        '''
        Search value in Binary tree
        val = Value need to search in binary tree
        '''
        temp = self.root
        flag = 0
        while temp:
            if val > temp.val:
                temp = temp.right
            elif val < temp.val:
                temp = temp.left
            else:
                flag = 1
                break
        if flag:
            print('{} value found in the tree'.format(val))
        else:
            print('{} value not found in the tree'.format(val))

    def traverse(self, current=1):
        '''
        Print all value of the tree in right side order
        '''
        if current == 1:
            current = self.root
        if current:
            print(current.val)
            self.traverse(current.right)
            self.traverse(current.left)