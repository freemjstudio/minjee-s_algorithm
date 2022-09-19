# 21610

n, m = map(int, input().split())
array = []
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]] # 구름 위치 표시하기
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m): # m회 시행
    d, s = map(int, input().split())
    next_clouds = []
    visited = [[False]*n for _ in range(n)]
    for cloud in clouds:
        x, y = cloud[0], cloud[1]
        nx = (n + x + dx[d-1]*s)%n # 1번행과 n번행이 이어져 있음
        ny = (n + y + dy[d-1]*s)%n # 1번열과 n번열이 이어져 있음
        next_clouds.append([nx, ny])

    # 2. 비내리기
    for cloud in next_clouds:
        x, y = cloud[0], cloud[1]
        array[x][y] += 1
        visited[x][y] = True
    # 3. 구름 제거
    clouds = []

    # 4. next_clouds에 있는 칸에서 대각선 방향으로 1 거리의 칸에서 물의 양이 증가함
    # 단, 이때는 1번열 & n번열 이어지지 x
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x, y = cloud[0], cloud[1]
        count = 0 # 대각선 거리 1 에 '물이 있는(array[i][j]>=1)'바구니의 수를 센다
        for k in range(4):
            nx = x + cx[k]
            ny = y + cy[k]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] >= 1:
                count += 1
        array[x][y] += count

    #5. 물의 양이 2 이상인 칸에 구름 생성하기
    for i in range(n):
        for j in range(n):
            if array[i][j] >= 2 and visited[i][j] == False:
                clouds.append([i, j])
                array[i][j] -= 2

result = 0
for i in range(n):
    result += sum(array[i])
print(result)