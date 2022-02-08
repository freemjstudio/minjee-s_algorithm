def insertion_sort(array):
    for end in range(1, len(array)):
        for i in range(end, 0, -1):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]

