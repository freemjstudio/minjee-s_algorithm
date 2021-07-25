a,b,c,d,e = map(int, input().split())
sum = a**2+b**2+c**2+d**2+e**2
print(sum%10)
a,b = map(int,input().split())

print(a*b)

# 먼저 숫자를 거꾸로 뒤집어야 한다
#그다음에 큰 수를 출력한다.

a, b = map(int, input().split())
read_a = (a%100)%10*100 + (a%100//10)*10 + a//100
read_b = (b%100)%10*100 + (b%100//10)*10 + b//100

if read_a > read_b:
    print(read_a)
else:
    print(read_b)

734 % 100 = 34
34 % 10 = 4