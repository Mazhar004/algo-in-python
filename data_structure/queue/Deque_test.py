from Deque import Deque
deque = Deque()
while True:
    try:
        t = int(input(
            'Press 1 to Left push\nPress 2 to Right push\nPress 3 to Left pop\nPress 4 to Right pop\nPress 5 to Show Items\nPress Enter to exit\n= '))
        if t == 1:
            deque.l_push(int(input('Enter value = ')))
        elif t == 2:
            deque.r_push(int(input('Enter value = ')))
        elif t == 3:
            print(deque.l_pop())
        elif t == 4:
            print(deque.r_pop())
        elif t == 5:
            temp = deque.head
            while temp:
                print(temp.val, end=' ')
                temp = temp.next
            print('\n')
        else:
            break
    except:
        break
