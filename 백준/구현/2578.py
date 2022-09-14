# 2578 빙고
import sys
array = dict()
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        array[a[j]] = (i,j) # 위치를 저장한다
check = [[0]*5 for i in range(5)] # 사회자가 숫자를 부를 때마다 지우기
answer = 0

for _ in range(5):
    bingo = list(map(int, input().split()))
    for i in range(5):
        answer += 1
        bingo_count = 0
        x, y = array[bingo[i]]
        check[x][y] = 1
        # 가로
        for j in range(5):
            if sum(check[j]) == 5: # 가로
                bingo_count += 1
            if sum([k[j] for k in check]) == 5: # 세로
                bingo_count += 1
        # 대각선 확인
        if check[0][0] + check[1][1] + check[2][2] + check[3][3] + check[4][4] == 5:
            bingo_count += 1
        if check[0][4] + check[1][3] + check[2][2] + check[3][1] + check[4][0] == 5:
            bingo_count += 1
        if bingo_count >= 3:
            print(answer)
            sys.exit()
