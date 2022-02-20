n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

max_result = 0
min_result = int(1e9)

def move(type, i):
    if type == 0: # down
        for j in range(n):
            array[i-1][j] += array[i][j]
    elif type == 1: # down left
        for j in range(n):
            array[i-1][j-1] += array[i][j]
    else: # down right
        for j in range(n):
            array[i-1][j+1] += array[i][j]


def dfs(count):
    if count == n-1:
        for j in range(n):
            max_result = max(max_result, array[n-1][j])
            min_result = min(min_result, array[n-1][j])
        return
    for type in range(3):
