from Queue import Queue
queue = Queue()
while True:
    try:
        t = int(input(
            'Press 1 to push\nPress 2 to pop\nPress 3 to show current length\nPress Enter to exit\n= '))
        if t == 1:
            data = map(int, (input('Enter space seperated values = ').split()))
            for i in data:
                queue.enqueue(i)
        elif t == 2:
            print(queue.dequeue())
        elif t == 3:
            print(len(queue))
        else:
            break
    except:
        break
