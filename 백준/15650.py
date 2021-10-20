# n 과 m

n, m = map(int, input().split())
array = []

def dfs(start):
    if len(array) == m:
        print(' '.join(map(str,array)))
        return
    for i in range(start, n+1):
        if i not in array:
            array.append(i)
            dfs(i+1)
            array.pop()

dfs(1)

