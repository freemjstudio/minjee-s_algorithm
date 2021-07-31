# 9012 번
import sys
N = int(sys.stdin.readline())



for i in range(N):
    b = input()
    s = list(b)
    sum = 0
    for j in s:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break

    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")


# 9012 번
import sys
N = int(sys.stdin.readline())

for i in range(N):

    s = input()
    stack = []
    cnt = 0
    for j in s:
        if j == '(':
            stack.append(j)
        elif j == ')':

            if len(stack) == 0:
                print("NO")
                cnt = -1
                break
            else:
                stack.pop()

    if len(stack) == 0 and cnt == 0:
        print("YES")
    elif len(stack) != 0 and cnt == 0:
        print("NO")

