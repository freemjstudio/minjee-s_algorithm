n = int(input())
a = list(map(int, input().split())) # 여러명일 수 있다.
b, c = map(int, input().split())
count = 0
for i in range(n):
    a[i] -= b
    count += 1

for i in range(n):
    if a[i] > 0:
        temp = a[i]//c

        if a[i]% c == 0:
            count += temp

        else:
            count += (temp + 1)


print(count)