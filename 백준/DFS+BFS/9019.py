
from collections import deque

def D(n):
    tmp = n*2
    if tmp > 9999:
        tmp %= 10000
    return tmp

def S(n):
    tmp = n
    if tmp == 0:
        return 9999
    tmp -= 1
    return tmp

def L(n):
    front = n%1000
    back = n//1000
    tmp = front*10 + back
    return tmp

def R(n):
    front = n%10
    back = n//10
    tmp = front*1000+back
    return tmp

def bfs(s, t): # start , target
    queue = deque()
    visited = set() # 우리가 DSLR 연산을 한번 할 때마다 생기는 결과를 저장해둔다.이미 계산된거라면 굳이 할필요 없으니까 절약된다.
    queue.append((s, ""))
    visited.add(s)
    while queue:
        n, op = queue.popleft()
        if n == t:
            print(op)
            return
        tmp = D(n)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"D"))

        tmp = S(n)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"S"))

        tmp = L(n)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"L"))

        tmp = R(n)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"R"))

for i in range(int(input())):
    start, target = map(int, input().split())
    bfs(start, target)

# list 로 만들었더니