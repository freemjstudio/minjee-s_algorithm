from collections import deque


# maps = n*m 배열
def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1:  # 통과 가능
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))
        return maps[n - 1][m - 1]

    answer = bfs(0, 0)
    if answer == 1:  # 마지막 칸 (n,m)이 1이면 값의 변화가 없다는 뜻 ! 즉 이동 못했음
        return -1
    else:
        return answer