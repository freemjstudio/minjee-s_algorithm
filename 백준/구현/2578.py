# 2578 빙고

array = []
for i in range(5):
    array.append(list(map(int, input().split())))
bingo = [] # 사회자
for i in range(5):
    bingo.append(list(map(int, input().split())))

def check():
    bingo_count = 0
    # 가로줄 체크
    for i in range(5):
        count = 0
        for j in range(5):
            if array[i][j] == 0:
                count += 1
        if count == 5:
            bingo_count += 1
    # 세로줄 체크
    for i in range(5):
        count = 0
        for j in range(5):
            if array[j][i] == 0:
                count += 1
        if count == 5:
            bingo_count += 1

    # 대각선 체크
    for i in range(5):
        count = 0
        for j in range(5):
            if i == j and array[i][j] == 0:
                count += 1
        if count == 5:
            bingo_count += 1

    for i in range(5):
        count = 0
        for j in range(5):
            if i + j == 4 and array[i][j] == 0:
                count += 1
        if count == 5:
            bingo_count += 1
    return bingo_count


