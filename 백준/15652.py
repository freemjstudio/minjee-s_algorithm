# 15652

n, m = map(int, input().split())

s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n+1):
        if i >= start:
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)