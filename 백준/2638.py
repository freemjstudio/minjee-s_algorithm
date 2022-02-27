# 2638 cheese
from collections import deque

n, m = map(int, input().split())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0 # result

def bfs():



print(count)