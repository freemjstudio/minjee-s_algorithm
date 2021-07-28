import sys
n = int(sys.stdin.readline())
points = []
for i in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))

points.sort(key=lambda a:(a[1],a[0]))

for i in points:
    print(i[0], i[1])