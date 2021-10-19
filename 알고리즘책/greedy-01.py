# 01 모험가 길드

n = int(input())
array = list(map(int, input().split()))

result = 0
count = 0 # 현재 그룹에 포함된 모험가의 수
array.sort()
for i in array:
    count += 1
    if count >= i: # 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 생성 가능 !!
        result += 1
        count = 0 # 모험가 수 초기화


print(result)