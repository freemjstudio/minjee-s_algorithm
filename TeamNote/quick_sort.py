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


def quick(a):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid -1)
        sort(mid, high)

    def partition(low, high):
        pivot = a[(low + high)//2]
        while low <= high:
            while a[low] < pivot:
                low += 1
            while a[high] > pivot:
                high -= 1
            if low <= high:
                a[low], a[high] = a[high], a[low]
                low, high = low +1, high -1
        return low
    return sort(0, len(a)-1)

quick(array)
print(array)