# 1074 py

N, r, c = map(int, input().split())

count = 0

def solve(N, x, y):
    global count
    if x == r and y == c:
        print(int(count))
        exit(0)

    if N == 1:
        count += 1
        return

    if not (x <= r < x + N and y <= c < y+N):
        count += N*N
        return

    solve(N/2, x,y)
    solve(N/2,x,y+N/2)
    solve(N/2,x+N/2,y)
    solve(N/2,x+N/2,y+N/2)

solve(2**N, 0, 0)