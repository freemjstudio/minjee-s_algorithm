# merge sort

array = [6,5,3,1,8,7,2,4]

def merge_sort(array):
    if len(array) < 2: # 원소가 하나인 경우
        return array
    merged_array = []
    mid = len(array)//2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    l = r = 0
    while l < len(left_array) and r < len(right_array):
        # 여기서는 작은 수 부터 정렬
        if left_array[l] < right_array[r]:
            merged_array.append(left_array[l])
            l += 1
        else:
            merged_array.append(right_array[r])
            r += 1
    merged_array += left_array[l:]
    merged_array += right_array[r:]
    return merged_array

print(array)
result = merge_sort(array)
print(result)

