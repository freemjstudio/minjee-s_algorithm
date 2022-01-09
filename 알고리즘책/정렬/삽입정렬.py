array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기 자신보다 작은 데이터를 만나면 그 자리에서 멈춤
            break

print(array)