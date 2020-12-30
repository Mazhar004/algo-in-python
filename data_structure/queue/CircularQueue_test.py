from CircularQueue import CircularQueue
cqueue = CircularQueue()
while True:
    try:
        t = int(input(
            'Press 1 to push\nPress 2 to pop\nPress 3 to show current length\nPress Enter to exit\n= '))
        if t == 1:
            data = map(int, (input('Enter space seperated values = ').split()))
            for i in data:
                cqueue.enqueue(i)
        elif t == 2:
            print(cqueue.dequeue())
        elif t == 3:
            print(len(cqueue))
        else:
            break
    except:
        break
