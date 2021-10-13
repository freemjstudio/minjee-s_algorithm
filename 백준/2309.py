# 2309 일곱 난쟁이
array = []

for i in range(9):
    array.append(int(input())) # 난쟁이의 키를 입력받음

total = sum(array)
one = 0
two = 0
for i in range(8):
    for j in range(i+1, 9):
        temp = array[i] + array[j]
        if total - temp == 100:
            one = array[i]
            two = array[j]

array.remove(one)
array.remove(two)
array.sort()
for i in array:
    print(i)
