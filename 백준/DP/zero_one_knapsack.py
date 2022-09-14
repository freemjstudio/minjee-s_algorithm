# 0-1배낭문제

# (value, weight)
cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]

def solve(cargo):
    capacity = 15 # 들 수 있는 무게 최대
    pack = []

    for i in range(len(cargo) + 1): # cargo 하나씩 확인
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i-1][1] <= c: # capacity
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c - cargo[i-1][1]],
                        pack[i-1][c]
                    )
                )
            else:# capacity 초과하면 이전 dp 값을 복붙
                pack[i].append(pack[i-1][c])
    return pack[-1][-1] # dp 결과