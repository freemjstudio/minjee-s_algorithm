# 115p 왕실의 나이트
data = input()
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1

types = [(-2,-1),(-2,1), (1,-2),(-1,-2), (2,1), (2,-1), (-1,2), (1,2)]

result = 0

for type in types:
    nx = x + type[0]
    ny = y + type[1]
    if nx >= 1 and ny >= 1 and nx <=8 and ny <=8:
        result += 1

print(result)