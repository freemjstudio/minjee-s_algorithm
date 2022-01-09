array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]: # 피벗보다 큰 데이터를 찾을 때까지 반복한다.
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오르쪽부분에서 각각 정렬 수행
    quick_sort(array, start, right-1) # 생각해보니까 현재 right가 pivot임 !
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)
