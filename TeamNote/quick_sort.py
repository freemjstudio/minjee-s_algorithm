def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    low, mid, high = [], [], []
    for i in a:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        else:
            mid.append(i)
    return quick_sort(low) + mid + quick_sort(high)

array = [6, 2, 9, 4, 1, 5, 3, 8]


print(quick_sort(array))