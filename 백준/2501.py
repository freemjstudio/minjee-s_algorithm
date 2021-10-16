n, k = map(int, input().split())
array = []
for i in range(1,n+1):
    if n%i == 0:
        array.append(i)

array.sort()
if len(array) < k:
    print(0)
else:
    print(array[k-1])