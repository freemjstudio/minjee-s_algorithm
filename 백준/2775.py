# 2775
T = int(input())
for i in range(T):
    floor = int(input())
    room = int(input())
    f0 = [x for x in range(1, room+1)] # 0 층
    for j in range(floor): # 층 수 만큼 반복
        for k in range(1, room): # 1 에서 n - 1 까지 인덱스로 사용
            f0[k] += f0[k-1] # 층별 각 호실의 사람 수를 변경한다.
    print(f0[-1]) # 가장 마지막 수를 출력한다.

