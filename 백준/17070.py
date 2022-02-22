# 17070 파이프 옮기기

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
result = 0  # 방법의 수

def dfs(x, y, dir):
    global result
    if x == n - 1 or y == n - 1:
        result += 1

    if dir == 0: # 가로
        if y < n-1 and array[x][y+1] == 0:
            dfs(x, y+1, 0) # -> 방향

        if x < n-1 and y < n-1 and array[x][y+1] == 0 and array[x+1][y+1] == 0 and array[x+1][y] == 0:
            dfs(x+1, y+1, 2) # \ 방향

    elif dir == 1: # 세로
        if x < n-1 and array[x+1][y] == 0: # 세로
            dfs(x+1, y, 1)

        if x < n-1 and y < n-1 and array[x][y+1] == 0 and array[x+1][y+1] == 0 and array[x+1][y] == 0: # 대각선
            dfs(x+1, y+1, 2)

    elif dir == 2: # 대각선
        if y < n-1 and array[x][y+1] == 0:
            dfs(x, y+1, 0) # 가로

        if x < n-1 and array[x+1][y] == 0: # 세로
            dfs(x+1, y, 1)

        if x < n-1 and y < n-1 and array[x][y + 1] == 0 and array[x + 1][y + 1] == 0 and array[x + 1][y] == 0:
            dfs(x + 1, y + 1, 2)


dfs(0,1,0)
print(result)