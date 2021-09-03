#1541 잃어버린 괄호

import sys

expression = sys.stdin.readline().split('-')
numbers = []

for exp in expression:
    count = 0
    temp = exp.split('+')
    for i in temp:
        count += int(i) # 현재 모두 str 이므로 변환해줘야 댐 ㅎㅎ
    numbers.append(count)

N = numbers[0]
for i in range(1, len(numbers)):
    N -= numbers[i]

print(N)





