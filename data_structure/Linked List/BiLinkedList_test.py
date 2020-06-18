from BiLinkedList import BiLinkedList
l_list = BiLinkedList()
while True:
    try:
        t = int(input(
            'Press 1 to append\nPress 2 to delete\nPress 3 to print\nPress 4 to print reverse order\nPress Enter to exit\n= '))
        if t == 1:
            data = int(input('Insert value for append = '))
            l_list.append(data)
        elif t == 2:
            data = int(input('Insert value you want to delete = '))
            l_list.delete(data)
        elif t == 3:
            l_list.traverse()
        elif t == 4:
            l_list.traverse(True)
        else:
            break
    except:
        break