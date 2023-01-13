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