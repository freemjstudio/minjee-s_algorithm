n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(n):
        if numbers[i] not in s:
            s.append(numbers[i])
            dfs(i+1)
            s.pop()

dfs(0) # index를 start로 넣는다