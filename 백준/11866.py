n, k = map(int, input().split())

array = [i for i in range(1, n+1)]
index = 0 # 제거될 사람의 인덱스 번호
result = []

for i in range(n):
    index += k-1
    if index >= len(array):
        index = index % len(array)
    result.append(str(array.pop(index)))

print("<", ", ".join(result)[:],">",sep='')