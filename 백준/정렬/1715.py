# 1715 정렬
import heapq

n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

result = 0
a.sort()
for i in range(n-1):
    temp = a[i] + a[i+1]
    result += temp
    a[i+1] = temp

print(result)
