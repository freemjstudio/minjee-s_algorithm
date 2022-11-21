import sys

sys.setrecursionlimit(10 ** 9)


def solution(places):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, step):
        if step == 2:
            return True
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if place[nx][ny] == 'O':
                    if dfs(nx, ny, step + 1) == False:  # 여기가 문제였음
                        return False
                elif place[nx][ny] == 'P':
                    return False

    for place in places:
        visited = [[False] * 5 for _ in range(5)]
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not visited[i][j]:
                    if dfs(i, j, 0) == False:
                        flag = False
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer