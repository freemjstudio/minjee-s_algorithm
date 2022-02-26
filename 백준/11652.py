# 11652 card

n = int(input())
card = {}

for _ in range(n):
    num = int(input())
    if num in card:
        card[num] += 1
    else:
        card[num] = 1

# value 값 오름차순
result = sorted(card.items(), key=lambda x : (-x[1], x[0]))

print(result[0][0])