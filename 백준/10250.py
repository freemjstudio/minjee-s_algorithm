#10250

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    H_list = [h for h in range(1,H+1)]
    W_list = [w for w in range(1,W+1)]
    count = 0

    for w in W_list:
        for h in H_list:
            room = h*100 + w
            count += 1
            if count == N:
                print(room)
                break