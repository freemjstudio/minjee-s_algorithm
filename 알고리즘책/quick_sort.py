
array = [5,2,3,4,1,6,8,7,9]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗 보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은데이터와 피벗을 교체한다.
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[pivot] = array[pivot], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right +1, end)

# quick_sort(array, 0, len(array) - 1)
print(array)

def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <=pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))
