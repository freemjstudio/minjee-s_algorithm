# 10825 국영수

n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[(n-1)//2])