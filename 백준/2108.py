import sys
from collections import Counter

n = int(sys.stdin.readline())

numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline()))

# 평균
print(round(sum(numbers)/n))

# 중앙값
numbers.sort()
print(numbers[len(numbers)//2])

# 최빈
count_dict = Counter(numbers)
modes = count_dict.most_common()

if len(modes) > 1:
    if modes[0][1] == modes[1][1]:
        mod = modes[1][0]
    else:
        mod = modes[0][0]
else:
    mod = modes[0][0]

print(mod)

# 범위
a = max(numbers) - min(numbers)
print(a)


