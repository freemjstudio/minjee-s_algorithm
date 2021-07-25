# 2609

a, b = map(int, input().split())
a_list = []
b_list = []
n = 1
max = 1 # 최대 공약수
min = 1 # 최소 공배수

while True:
    if a%n == 0 and b%n == 0:
        a_list.append(n)
    if a < b:
        if a == n:
            break
    else:
        if b == n:
            break
    n += 1

for i in a_list:
    max *= i
print(max)

min = max * a/max * b/max
print(min)


# 다른 풀이
a, b = map(int, input().split())
a_list = []
b_list = []
n = 1
n_b = 1
min_R = 1
max_R = 1
while True:
    if a % n == 0:
        a_list.append(n)
    if a == n:
        break
    n += 1

while True:
    if b % n_b == 0:
        b_list.append(n_b)
    if b == n_b:
        break
    n_b += 1

max_list = list(set(a_list) & set(b_list))
max_R = max(max_list)
print(max_R)
min_R = a*b//max_R
print(min_R)


