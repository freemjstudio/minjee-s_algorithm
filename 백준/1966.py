T = int(input()) # test case

for i in range(T):
    N, M = map(int, input().split())

    order = list(map(int, input().split())) # 중요도
    index = [0 for i in range(N)] # 위치를 저장하는 리스트
    index[M] = 1
    count = 0
    while True:
        if order[0] == max(order):
            count += 1
            if index[0] == 1:
                print(count)
                break
            else:
                del order[0]
                del index[0]
        else:
            order.append(order[0])
            del order[0]
            index.append(index[0])
            del index[0]
