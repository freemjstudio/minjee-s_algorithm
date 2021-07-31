# 10866 deque

import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        d.appendleft(command[1])
    elif command[0] == 'push_back':
        d.append(command[1])
    elif command[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif command[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif command[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
