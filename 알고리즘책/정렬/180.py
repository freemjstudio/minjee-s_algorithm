n = int(input())
array = []
# for i in range(n):
#     name, score = input().split()
#     score = int(score)
#     array.append((score, name))
#
# array.sort()
#
# for i in range(n):
#     print(array[i][1], end=' ')

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda student:student[1])

for student in array:
    print(student[0], end=' ')