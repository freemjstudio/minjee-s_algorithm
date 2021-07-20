# 5585 거스름돈

n = int(input()) #지불할 돈
money = 1000 - n # 받을 잔돈
cnt = 0
while money == 0:
    if money >= 500:
        money -= 500
        cnt += 1
    elif money < 500 and money >= 100:
        money -= 100
        cnt +=1
    elif money < 100 and money >= 50:
        money -= 50
        cnt += 1
    elif money < 50 and money >= 10:
        money -= 10
        cnt += 1
    elif money < 10 and money >= 5:
        money -= 5
        cnt += 1
    elif money < 5:
         money -= 1
         cnt += 1
print(cnt)


a = 1000 - int(input())
b = [500,100,50,10,5,1]
count = 0
for i in b:
    count += a//i
    a %= i

print(count)

a, b = map(int, input().split())
print(a+b)