# 14888
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

op_real = []

for i in range(len(op)):
    if op[i] != 0:
        if i == 0:
            op_real.append('+'*op[i])
        elif i == 1:
            op_real.append('-' * op[i])
        elif i == 2:
            op_real.append('*' * op[i])
        elif i == 3:
            op_real.append('//' * op[i])

permute = permutations(op_real) # 연산자들을 나열하는 방법

max = 0
min = sum(numbers)
result = numbers[0]

for p in list(permute):
    for i in range(n):
        op1 = p[i]
        if op1 == '+':
            result += numbers[i]
        elif op1 == '-':
            result -= numbers[i]
        elif op1 == '*':
            result *= numbers[i]
        elif op1 == '//':
            result //= numbers[i]
    if result > max:
        max = result
    if result < min:
        min = result


print(min)
print(max)