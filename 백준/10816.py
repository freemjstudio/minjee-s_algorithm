# 10816 숫자카드

N = int(input())
cards = list(map(int, input().split()))
cards_count = {} # 딕셔너리로 개수 세기
for i in cards:
    if cards_count.get(i) == None:
        cards_count[i] = 1
    else:
        cards_count[i] += 1

M = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    if cards_count.get(i) == None:
        print('0', end=' ')
    else:
        print(cards_count.get(i), end=' ')