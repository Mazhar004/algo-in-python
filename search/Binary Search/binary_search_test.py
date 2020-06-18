from binary_search import binary
import numpy as np

size = 10
arr = np.random.randint(1, 100, size=(size))
arr = sorted(arr)
print(arr)

while True:
    try:
        find = int(input('Enter value to search or enter "q" to Exit = '))
    except:
        break
    val = binary(arr, find, 0, size)
    if val != -1:
        print('\n{} found at {} position in {}\n'.format(find, val, arr))
    else:
        print('\n{} not found in {}\n'.format(find, arr))
