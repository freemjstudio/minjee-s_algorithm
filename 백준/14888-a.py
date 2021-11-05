
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

#  최댓값과 최솟값
min_value = 1e9
max_value = -1e9

# dfs 탐색 매소드

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우 최솟값과 최댓값 업데이트

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now+numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / numbers[i]))
            div += 1

dfs(1,numbers[0])

print(max_value)
print(min_value)


