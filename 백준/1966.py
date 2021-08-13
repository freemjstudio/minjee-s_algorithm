T = int(input()) # test case

for i in range(T):
    N, M = map(int, input().split())

    order = list(map(int, input().split())) # 중요도
    index = [0 for i in range(N)] # 위치를 저장하는 리스트
    index[M] = 1
    count = 0
    while True:
        if order[0] == max(order): # 맨 처음 요소 중요도가 가장 큰 경
            count += 1
            if index[0] == 1: # M 번째 출력물이었다면 !! 우리가 찾는게 맞으니
                print(count) # 몇 번째로 출력할지 count 를 출력한다 !
                break
            else:
                del order[0] # 아니면 바로 pop 시켜버린다 ! 그니까 바로 출력한다는 뜻임 여기서는 ㅇㅇ
                del index[0]
        else: # 중요도가 더 큰게 있었다면
            order.append(order[0]) # 큐 맨 뒤로 보내버림
            del order[0]
            index.append(index[0]) # 큐 맨 뒤로 보내버림 order랑 싱크 맞춰줘야댐 ㅇㅇ 
            del index[0]
