from BinaryTree import BinaryTree
tree = BinaryTree()
while True:
    try:
        t = int(input('Press 1 to insert\nPress 2 to search\nPress 3 to print\nPress Enter to exit\n= '))
        if t == 1:
            data = int(input('Give value to insert = '))
            tree.insert(data)
        elif t == 2:
            data = int(input('Give value to search in tree = '))
            tree.search(data)
        elif t == 3:
            tree.traverse()
        else:
            break
    except:
        break