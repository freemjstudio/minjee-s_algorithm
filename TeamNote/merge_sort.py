def merge_sort(a):
    def sort(low, high):
        if high - low < 2: # 배열의 크기가 2보다 작다
            return
        mid = (low + high)//2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = [] # 공간 복잡도는 O(N)
        l, h = low, mid

        while l < mid and h < high:
            if a[l] < a[h]:
                temp.append(a[l])
                l += 1
            else:
                temp.append(a[h])
                h += 1

        while l < mid:
            temp.append(a[l])
            l += 1
        while h < high:
            temp.append(a[h])
            h += 1

        for i in range(low, high):
            a[i] = temp[i - low] # 병합 결과를 실제 배열에 옮긴다
    return sort(0, len(a))

array = [1,5,3,7,11,2]
merge_sort(array)
print(array)