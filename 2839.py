# 2839
n = int(input())
bag = 0
while n >=0 :
    if n % 5 == 0 : # 5의 배수이면
        bag += (n//5)
        print(bag)
        break
    n -= 3
    bag += 1
else : # while 문이 거짓으로 판정되는 경우 else에 걸린다 대박..!
    print(-1)