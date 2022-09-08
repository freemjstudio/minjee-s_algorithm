import sys

sys.setrecursionlimit(10 ** 6)


def dfs(start, visited, computers, n):
    # start : 시작 노드
    visited[start] = True
    for i in range(n):
        if visited[i] == False and computers[start][i] == 1:
            visited = dfs(i, visited, computers, n)
    return visited


def solution(n, computers):
    answer = 0
    visited = [False] * n
    # 그래프 탐색 알고리즘
    for start in range(n):
        if visited[start] == False:
            dfs(start, visited, computers, n)  # dfs 실행하기
            answer += 1  # dfs 실행한 횟수만큼 + 1

    return answer