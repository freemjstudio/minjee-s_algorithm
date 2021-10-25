n = int(input())
k = int(input())

board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())

l = int(input())

for _ in range(l):
    x, y = input().split()

