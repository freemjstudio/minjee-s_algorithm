def selection_sort(a):
    for i in range(len(a)-1): # 맨 마지막 원소는 자연스럽게 정렬이 되므로 n-1
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

array = [4,2,8,1,9]

selection_sort(array)
print(array)