# 수들의 합

S = int(input())

num = 1

while True:

    S -= num
    if S <= num:
        break
    num += 1

print(num)