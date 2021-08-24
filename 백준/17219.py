#17219
import sys

N, M = map(int, sys.stdin.readline().split())
password = {}

for i in range(N):
    k, v = sys.stdin.readline().split()
    password[k] = v

for i in range(M):
    print(password[sys.stdin.readline().rstrip()])
