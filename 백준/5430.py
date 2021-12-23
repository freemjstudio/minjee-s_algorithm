#5430 AC
import sys
from collections import deque

T = int(input())
for _ in range(T):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    array = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(array) # list -> queue type
    flag = 0
    count = 0

    if n == 0:
        queue = []

    for cur in command:
        if cur == 'R':
            count += 1
        elif cur == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if count%2 == 0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")




