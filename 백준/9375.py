# 9375

T = int(input())
for _ in range(T):
    N = int(input())
    clothes = dict()

    if N == 0:
        print(0)
        continue

    for i in range(N):
        wear_name, wear_type = map(str, input().split())

        if wear_type in clothes.keys():
            clothes[wear_type] += 1
        else:
            clothes[wear_type] = 1
        result = 1
        for key in clothes.keys():
            result *= clothes[key]+1
    print(result-1)



