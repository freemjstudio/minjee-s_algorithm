#2331 반복 수열

a, p = map(int, input().split())
array = [a]

while True:
    temp = 0
    for i in str(array[-1]):
        temp += int(i)**p

    if temp in array:
        break  # 반복수열의 시작
    array.append(temp)
print(array.index(temp))