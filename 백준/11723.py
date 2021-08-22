#11723
import sys

S = set()
N = int(sys.stdin.readline())

for i in range(N):

    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
        continue

    command, data = temp[0], temp[1]
    data = int(data)

    if command == 'add':
        S.add(data)
    elif command == 'check':
        print(1 if data in S else 0)
    elif command == 'remove':
        S.discard(data)
    elif command == 'toggle':
        if data in S:
            S.discard(data)
        else:
            S.add(data)