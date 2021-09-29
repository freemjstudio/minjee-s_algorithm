N = int(input())

array = []

for _ in range(N):
    name, score = input().split()
    score = int(score)
    array.append((name, score))

array = sorted(array, key=lambda student: student[1]) # key를 이용하여 점수를 기준으로 정렬한다

for student in array:
    print(student[0], end=' ')