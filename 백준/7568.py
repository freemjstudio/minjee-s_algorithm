# 7568
n = int(input()) # 전체 사람의 수
students = []

for i in range(n):
    x, y = map(int, input().split())
    students.append((x,y))

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end= " ")

