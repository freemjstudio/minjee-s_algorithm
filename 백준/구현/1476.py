# 1476 번 날짜계산

e, s, m = map(int, input().split())

a, b, c = 1, 1, 1 # 초기값
count = 1

while True:
    if a == e and b == s and c == m:
        print(count)
        break

    if a == 15:
        a = 1
    else:
        a += 1
    if b == 28:
        b = 1
    else:
        b += 1
    if c == 19:
        c = 1
    else:
        c += 1
    count += 1