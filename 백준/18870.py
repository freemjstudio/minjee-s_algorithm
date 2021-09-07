# 18870
import sys
input = sys.stdin.readline
N = int(input())
points = list(map(int, input().split()))
sorted_points = sorted(list(set(points)))
dic = {sorted_points[i] : i for i in range(len(sorted_points))}
for point in points:
    print(dic[point], end=' ')

