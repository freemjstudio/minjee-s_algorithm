n = input().rstrip()

temp1 = 0
temp2 = 0

for i in n[:len(n)//2]:
    temp1 += int(i)

for i in n[len(n)//2:]:
    temp2 += int(i)

if temp1 == temp2:
    print('LUCKY')
else:
    print('READY')

# 다른 풀이

n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length //2):
    summary += int(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")