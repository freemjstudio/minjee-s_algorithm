# 삽입 정렬 코드

array = [5,2,3,4,1,6,8,7,9]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j]< array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)