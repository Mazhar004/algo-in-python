def binary(array, val, start, end):
    '''
    array = Enter a sorted array
    val   = value user want to find
    start = starting index of an array
    end   = ending index of an array
    '''
    if end <= start:
        return -1
    mid = (start+end)//2
    if array[mid] == val:
        return mid
    elif array[mid] > val:
        end = mid
    else:
        start = mid+1
    return binary(array, val, start, end)
