# 2292 벌집

N = int(input())

count_six = 6
temp = 1
count = 1
while temp < N:
    temp = temp + count_six
    count += 1
    count_six += 6

print(count)
