# 11650
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

#points.sort()
points.sort(key=lambda point:(point[0],point[1]))
for i in points:
    print(i[0], i[1])


# 왜 lambda는 안되는걸까,,