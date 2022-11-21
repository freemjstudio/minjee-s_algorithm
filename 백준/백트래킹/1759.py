from collections import deque


def solution(begin, target, words):
    answer = 0
    if target in words:
        # bfs 실행
        queue = deque()
        queue.append((begin, 0))
        n = len(begin)  # 단어의 길이
        visited = [False] * len(words)  # 방문 여부 표시하기

        while queue:
            now, step = queue.popleft()
            if now == target:
                return step
            for i in range(len(words)):
                if visited[i] == False:  # 아직 방문하지 않은 경우
                    count = 0
                    for j in range(n):  # 글자 하나씩 체크
                        if now[j] == words[i][j]:
                            count += 1
                        if count >= n - 1:
                            visited[i] = True
                            queue.append((words[i], step + 1))
    else:
        return answer