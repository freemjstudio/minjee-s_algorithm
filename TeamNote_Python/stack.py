# 10828 stack 구조
import sys
n = int(input())
stack = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == "size":
        print(len(stack))

    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)