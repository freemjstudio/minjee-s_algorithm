# 별찍기 11

n = int(input())

graph = [[' ']*2*n for _ in range(n)]

def star(x, y, n):
    if n == 3:
        graph[x][y] = '*'
        graph[x+1][y-1] = graph[x+1][y+1] = '*'
        for i in range(-2, 3):
            graph[x+2][y+i] = '*'
    else:
        NEXT = n//2
        star(x, y, NEXT)
        star(x+NEXT, y+NEXT, NEXT)
        star(x+NEXT, y-NEXT, NEXT)

star(0, n-1, n)
for i in graph:
    print("".join(i))
