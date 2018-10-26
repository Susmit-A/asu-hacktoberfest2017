def selection(array):
    size = len(array)
    for i in range(size-1):
        least = array[i]
        count = i
        for j in range(i+1, size):
            if least > array[j]:
                least = array[j]
                count = j

        temp = array[i]
        array[i] = array[count]
        array[count] = temp

    return array
