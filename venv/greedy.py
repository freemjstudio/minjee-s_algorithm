n = 1260
coin_array = [500, 100, 50, 10]
count = 0 # 쓰인 동전 개수
for coin in coin_array:
    count += n // coin # 해당 화폐로 거슬러줄 수 있는 동전 개수
    n %= coin # 거슬러준 다음 남은 금액

print(count)