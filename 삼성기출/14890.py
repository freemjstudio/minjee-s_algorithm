# 경사로

n, l = map(int, input().split())
array = []

def check(a):
    visited = [False for i in range(n)] # 경사로 설치 여부 !!!!!
    for i in range(n-1):
        if a[i] == a[i+1]:
            continue
        if abs(a[i] - a[i+1]) > 1:
            return False
        if a[i] > a[i+1]:
            temp = a[i+1] # 더 낮은 층
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if a[j] != temp:
                        return False
                    if visited[j] == True: # 이미 경사로가 설치되어 있는가 ?
                        return False
                    visited[j] = True
                else:
                    return False
        else:
            temp = a[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if a[j] != temp:
                        return False
                    if visited[j] == True:
                        return False
                    visited[j] = True
                else:
                    return False
    return True


for i in range(n):
    array.append(list(map(int, input().split())))

total = 0
for i in array:
    if check(i):
        total += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(array[j][i])
    if check(temp):
        total += 1

print(total)