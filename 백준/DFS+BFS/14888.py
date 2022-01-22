# 연산자 끼워넣기


n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = -1e9
min_result = 1e9

def dfs(i , now):
    global min_result, max_result, add, sub, mul, div

    if i == n:
        max_result = max(now, max_result)
        min_result = min(now, min_result)

    if add > 0:
        add -= 1
        dfs(i+1, now+data[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, now-data[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, now*data[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, int(now/data[i]))
        div += 1



dfs(1,data[0])


print(max_result)
print(min_result)