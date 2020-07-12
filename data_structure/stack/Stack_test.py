from Stack import Stack
stack = Stack()
while True:
    try:
        t = int(input(
            'Press 1 to push\nPress 2 to pop\nPress 3 to peek\nPress Enter to exit\n= '))
        if t == 1:
            data = map(int, (input('Enter space seperated values = ').split()))
            for i in data:
                stack.push(i)
        elif t == 2:
            print(stack.pop())
        elif t == 3:
            print(stack.peek())
        else:
            break
    except:
        break
