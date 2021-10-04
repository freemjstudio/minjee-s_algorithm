N = int(input())
array = list(map(int, input().split())) # 부품 입력받기
array.sort()
M = int(input())
X = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

for i in X:
    result = binary_search(array, i, 0, N-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

