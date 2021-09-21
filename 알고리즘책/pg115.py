# 2. 왕실의 나이트
pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord('a')) + 1 # 문자 abcdefgh 를 숫자로 바꿔야 한다 !!! 와 이게 대박이네


steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)] # 움직일 수 있는 방법의 경우의 수
result = 0

for step in steps:
    nr = row + step[0]
    nc = col + step[1]
    if nr >=1 and nr <= 8 and nc >= 1 and nc <= 8:
        result += 1

print(result)

