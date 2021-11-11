n = int(input())
array = list(map(int, input()))

def binary(array, start, end):
    if start > end:
        return None
    mid = (start + end) //2 # 얘가 인덱스 역할을 한다.
    if array[mid] == mid:
        return mid
    elif mid < array[mid]:
        binary(array, mid+1, end)
    else:
        binary(array, start, mid -1)

index = binary(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)






