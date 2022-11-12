# 비트 마스킹
import sys
input = sys.stdin.readline
print(bin(1<<20)) # 0b100000000000000000000
n, m = map(int, input().split())
train = [0] * n
for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        i, x = op[1]-1, op[2]-1 # 탑승하기
        train[i] = train[i] | 1 << x # | bit 단위 or 연산
    elif op[0] == 2: # 제거하기
        i, x = op[1] - 1, op[2] - 1
        train[i] = train[i] & ~(1 << x)
        # x 자리에 1이되고 나머지는 0 
    elif op[0] == 3:
        i = op[1] -1
        train[i] = train[i] << 1 # 왼쪽으로 비트 밀기
        train[i] = train[i] & ~(1 << 20)
        # 0011 -> 0110
        # 1000 -> ~(1000) : 0111
        # bin(1 << 20) : 100000000000000000000
    elif op[0] == 4:
        i = op[1] - 1
        train[i] = train[i] >> 1 # 오른쪽으로 비트 밀기
        # 0100 -> 0010
    train[i]

print(len(set(train)))