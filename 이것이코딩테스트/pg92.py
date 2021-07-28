# 큰 수의 법칙
n,m,k = map(int, input().split()) # 첫 줄 입력받기 , n 개의 자연수가 입력된다.
data = list(map(int, input().split())) # 숫자 데이터 입력받기
data.sort() # 입력 받은 데이터를 오름차순으로 정렬한다.
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0 # 계산 결과 저장
while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)


# 다른 풀이

n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

result = 0
count = int(m/(k+1)) * k
count += m % (k+1) # 나머지
result += count * first
result += (m - count) * second # 두번째로 큰 수 더하기 
print(result)


