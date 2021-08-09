#10773
K = int(input())

stack = []
result = 0

for i in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
        result += num
    elif num == 0:
        result -= stack.pop()

print(result)