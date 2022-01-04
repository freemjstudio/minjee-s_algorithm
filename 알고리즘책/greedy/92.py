import heapq

'''
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))


heap = []

first = 0 # 가장 큰 수
second = 0  # 두번째로 큰 수

for number in numbers:
    heapq.heappush(heap, (-number, number)) # (우선순위, 값) -> 파이썬은 최소 힙을 지원하기 때문
    
first = heapq.heappop(heap)
second = heapq.heappop(heap)

count = 0 
result = 0
cnt_k = 0 # k 카운트 

while True :
    if cnt_k == k:
        result += second
        cnt_k = 0
    else:
        result += first
        cnt_k += 1
    if count == m:
        print(result)
        break
'''
# 정답 예시 1

'''
result = 0
numbers.sort() 
first = numbers[n-1] # 가장 큰 수 
second = numbers[n-2] # 두번째로 큰 수 

while True:
    for i in range(k): 
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break 
    result += second 
    m -= 1 

print(result)
'''

# 정답 예시 2
'''
result = 0
numbers.sort()
first = numbers[n-1] # 가장 큰 수
second = numbers[n-2] # 두번째로 큰 수


 #큰 수가 더해지는 횟수를 카운트 한다.
count = int(m/(k+1))*k
count += m%(k+1)

result += first*count
result += second*(m-count)
print(result)
'''

m = 8
k = 3
count = int(m/(k+1))*k
print(count)
count += m%(k+1)
print(count)

