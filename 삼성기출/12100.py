# 12100 - 2048
import copy

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 상하좌우 이동시키기
check = [[0]*n for _ in range(n)] # 이미 합쳐진 블록인지 확인하기
result = 0
def move_block(type):
    if type == 0 : # up

    elif type == 1: # down

    elif type == 2: # left
    else: # right


def dfs(count):
    global array
    if count == 5:
        for i in range(n):
            for j in range(n):
                result = max(result, array[i][j])
        return

    temp_array = copy.deepcopy(array)
    for i in range(4):
        move_block(i)
        dfs(count+1)
        array = copy.deepcopy(temp_array)

dfs(0)
print(result)