for tc in range(int(input())):
    n = int(input())
    data = []
    for i in range(n):
        a, b = map(int, input().split())
        data.append((a, b))
    data.sort()
    MAX = data[0][1]
    count = 1 # 1차에서 1등한 사람은 무조건 뽑히기 때문이다.
    for i in range(1, n):
        if MAX > data[i][1]:
            count += 1
            MAX = data[i][1]
    print(count)