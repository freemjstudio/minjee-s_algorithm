# https://www.acmicpc.net/problem/1244

n = int(input()) # 스위치의 개수
data = list(map(int, input().split()))
m = int(input()) # 학생 수
for _ in range(m):
    gender, number = map(int, input().split())
    if gender == 1: # 남학생인 경우
        for i in range(number-1, n, number):
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0
    else: # 여학생인 경우
        number -= 1 # index에 맞추기
        k = 0
        while True:
            if number - k < 0 or number + k > n-1:
                break
            if data[number - k] == data[number + k]:
                k += 1
            else:
                break
        k -= 1
        for i in range(number-k, number+k+1):
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0

for i in range(n):
    print(data[i], end= " ")
    if (i+1) % 20 == 0:
        print()