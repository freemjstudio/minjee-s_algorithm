import math

n = 1000 # 2 ~ 1000 까지의 모든 소수
array = [True]*(n+1) # 아리스토테네스의 체
for i in range(2, int(math.sqrt(n))+1): # 제곱수까지만 확인한다
    if array[i]:
        j = 2
        while i*j < n: # n 보다 작은 모든 i의 배수를 지운다
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=" ")