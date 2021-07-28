# 수 정렬하기
import sys
n = int(sys.stdin.readline())
result = [0 for _ in range(10001)]
for _ in range(n):
    num = int(sys.stdin.readline())
    result[num] += 1

for i in range(len(result)):
    for j in range(result[i]):
        print(i) # 중복되는 숫자 있으면 1 1 1 그거 다 출력 ! 인덱스를 숫자라고 생각하는거지 

