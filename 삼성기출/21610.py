# 21610

n, m = map(int, input().split())
array = []
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)] # 구름 위치 표시하기
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m): # m회 시행
    d, s = map(int, input().split())
    # 1. 구름 이동
    for i in len(cloud):
        for _ in range(s):
            cloud[i][0] = cloud[i][0] + dx[d]
            cloud[i][1] = cloud[i][1] + dy[d]
    # 2. 비내리기
    for i in len(cloud):

print(sum(array))