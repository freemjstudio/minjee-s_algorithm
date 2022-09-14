# https://www.acmicpc.net/problem/1010
import math
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    result = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
    print(result)

