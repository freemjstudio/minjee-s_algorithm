from collections import defaultdict


def solution(tickets):
    answer = []
    n = len(tickets)
    graph = [[] * n]
    for i in range(n):
        graph[tickets[i][0]].append(tickets[i][1])
    visited = defaultdict(bool)
    for i in range(n):
        visited[graph[i]] = False

    def dfs(start, path):
        if len(path) == n + 1:
            return path

        visited[start] = True  # 방문 처리
        path.append(start)
        for next in graph[start]:
            if visited[next] == False:
                dfs(next)

    dfs("INC", answer)

    return answer