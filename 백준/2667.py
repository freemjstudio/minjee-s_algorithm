# 2667
N = int(input())
array = []
num = []
for _ in range(N):
    array.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= N or y >= N:
        return False

    if array[x][y] == 1: # 집 발견
        global count
        count += 1
        array[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False

result = 0
count = 0

for i in range(N):

    for j in range(N):
        if dfs(i,j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])

