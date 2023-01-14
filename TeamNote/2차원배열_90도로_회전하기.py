# 6
# 3 3 3 3 3 3
# 2 3 3 3 3 3
# 2 2 2 3 2 3
# 1 1 1 2 2 2
# 1 1 1 3 3 1
# 1 1 2 3 3 2

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

new_array = list(map(list, zip(*array[::-1])))

#print(*array[::-1])
# [1, 1, 2, 3, 3, 2] [1, 1, 1, 3, 3, 1] [1, 1, 1, 2, 2, 2] [2, 2, 2, 3, 2, 3] [2, 3, 3, 3, 3, 3] [3, 3, 3, 3, 3, 3]
# zip 을 안쓰면 리스트 안에 묶이지 않음 즉 n개 1차원 배열 여러개임

print(list(map(list, zip(*array[::-1]))))