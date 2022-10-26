array = [
[0 ,0 ,0 ,0, 0],
[4 ,4 ,4 ,4, 4],
[3 ,3 ,3 ,3, 3],
[2 ,2 ,2 ,2, 2],
[1 ,1 ,1 ,1 ,1]]

n = 5
for i in range(n):
    print(array[i])

print()
for i in range(-1, -n, -1):
    array[i] = array[i-1]
array[0] = [0 for i in range(n)]

for i in range(n):
    print(array[i])

