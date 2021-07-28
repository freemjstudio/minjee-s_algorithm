#1920 수 찾기


# 이렇게 풀이하면 시간초과가 난다.. 백준은 시간초과 날때 보통 내장 함수를 써서 나는 경우가 많은 것 같다.
# 풀이를 찾아봤는데 이렇게.. 하니까 되던뎅 사실 다른 점은 집합으로 처리한거랑,

# for i in M:
#     stdout.write('1\n') if i in N else stdout.write('0\n')

# 이진탐색 으로 풀어보기

import sys
n = sys.stdin.readline()
N = sorted(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
M = map(int, sys.stdin.readline().split())


def binary(num, N, start, end):
    if start > end:
        return 0
    m = (start + end)//2
    if num == N[m]:
        return 1
    elif num < N[m]:
        return binary(num, N, start, m-1)
    else:
        return binary(num, N, m+1, end)

for i in M:
    start = 0
    end = len(N)-1
    print(binary(i,N,start,end))
