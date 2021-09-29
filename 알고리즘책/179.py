N = int(input())

array = []

for _ in range(N):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')