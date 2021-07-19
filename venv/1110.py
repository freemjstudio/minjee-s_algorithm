# 1110 더하기 사이클

n = int(input()) # 주어지는 숫자
num = n
count = 0
result = 0
temp = 0

while True:
    temp = n//10 + n%10
    result = (n%10)*10 + temp%10
    count += 1
    n = result # 여기가 포인트네 !
    if result == num:
        break
print(count)


