# 16987 계란으로 계란치기

eggs = [] # 계란 정보 리스트

n = int(input())
for _ in range(n):
    s, w = map(int, input().split())
    eggs.append([s, w])

answer = 0

def break_egg(idx):
    global answer
    if idx == n: # 손에 든 계란이 가장 오른쪽 계란(맨 마지막 인덱)인 경우 종료한다
        count = 0 # 꺠진 계란 개수 세기
        for i in range(n):
            if eggs[i][0] <= 0:
                count += 1
        answer = max(answer, count)
        return

    # 계란이 모두 깨져있는지 확인
    flag = True
    for i in range(n):
        if i == idx:
            continue
        if eggs[i][0] > 0:
            flag = False
    if flag:
        answer = max(answer, n-1)
        return

    for i in range(n):
        if i == idx:
            continue
        if eggs[i][0] <= 0: # 이미 깨진 계란은 pass한다
            continue
        eggs[idx][0] -= eggs[i][1] # s1 - w2
        eggs[i][0] -= eggs[idx][1] # s2 - w1
        break_egg(idx+1)
        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]


break_egg(0)
print(answer)