# 1987 알파벳
r, c = map(int, input().split())
array = []
for _ in range(r):
    array.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1
alphabet = []
def dfs(x, y, cnt):

    global count
    count = max(cnt, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if array[nx][ny] not in alphabet:
                alphabet.append(array[nx][ny])
                dfs(nx, ny, cnt+1)
                alphabet.pop()

dfs(0, 0, 1)
print(count)