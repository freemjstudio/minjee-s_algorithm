# 12100 - 2048
import copy

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 상하좌우 이동시키기

result = 0
def move_block(type):
    if type == 0: # up
        for j in range(n):
            index = 0
            for i in range(1, n):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0

                    if temp == array[index][j]:
                        array[index][j] = temp*2
                        index += 1

                    elif array[index][j] == 0:
                        array[index][j] = temp

                    else: # 숫자 다른 경우
                        index += 1
                        array[index][j] = temp

    elif type == 1: # down
        for j in range(n):
            index = n-1
            for i in range(n-2, -1, -1):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0

                    if temp == array[index][j]:
                        array[index][j] = temp*2
                        index -= 1

                    elif array[index][j] == 0:
                        array[index][j] = temp

                    else:
                        index -= 1
                        array[index][j] = temp
    elif type == 2: # right
        for i in range(n):
            index = n-1
            for j in range(n-2, -1, -1):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0

                    if temp == array[i][index]:
                        array[i][index] = temp*2
                        index -= 1

                    elif array[i][index] == 0:
                        array[i][index] = temp

                    else:
                        index -= 1
                        array[i][index] = temp

    else: # left
        for i in range(n):
            index = 0
            for j in range(1, n):
                if array[i][j]:
                    temp = array[i][j]
                    array[i][j] = 0

                    if temp == array[i][index]:
                        array[i][index] = temp*2
                        index += 1
                    elif array[i][index] == 0:
                        array[i][index] = temp
                    else:
                        index += 1
                        array[i][index] = temp


def dfs(count):
    global array, result
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