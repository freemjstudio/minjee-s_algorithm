array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0]* (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

a = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(a, key=setting)
print(result)

