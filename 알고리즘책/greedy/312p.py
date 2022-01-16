# 곱하기 혹은 더하기

s = input()
n = len(s)
temp = int(s[0])
for i in range(1, n):
    if int(s[i-1]) == 0:
        temp += int(s[i])
    else:
        temp *= int(s[i])
print(temp)
