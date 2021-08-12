# 1874

N = int(input())
count = 1 # stack number 오름차순으로 증가
stack = []
op = []
temp = True


for i in range(N):
    number = int(input()) # 들어오는 숫자
    while count <= number:
        stack.append(count)
        op.append("+")
        count += 1
    if stack[-1] == number:
        stack.pop()
        op.append("-")
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)













