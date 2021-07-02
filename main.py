a = float(input())
print(format(a, ".2f"))

#소수점 이하 두번째 자리까지 반올림
# format(숫자, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림
f1, f2 = input().split()
result = float(f1)/float(f2)
print(format(result, ".3f"))

a, b = input().split()
n1 = int(a)
n2 = int(b)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1//n2)
print(n1%n2)
print(format(n1/n2, ".2f"))

a, b, c = input().split()
n1 = int(a)
n2 = int(b)
n3 = int(c)
sum = n1+n2+n3
mean = sum/3
print(sum, format(mean, ".2f"))

n = int(input())
print(n<<1) # 10을 2배한 값
print(n>>1)
print(n<<2)
print(n<<2)

a, b = input().split()
n1 = int(a)
n2 = int(b)
print(bool(int(a)) and bool(int(b)))
n = bool(int(input()))
print(not n)

a, b = input().split()
n1 = int(a)
n2 = int(b)
if (n1 == True) or (n2 == True):
    print(True)
else:
    print(False)


a, b = input().split()
n1 = bool(int(a))
n2 = bool(int(b))
print((n1 and (not n2)) or (not n1) and n2)

a, b = input().split()
n1 = bool(int(a))
n2 = bool(int(b))
if n1 == n2:
    print(True)
else:
    print(False)

a, b = input().split()
n1 = bool(int(a))
n2 = bool(int(b))
print((n1 == False) and (n2 == False))


n = input()
m = int(n)
print(~m)

n1, n2, n3 = input().split()
a = int(n1)
b = int(n2)
c = int(n3)

print((a if a<b else b) if ((a if a<b else b)<c) else c)

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2 == 0:
    print("even")
else:
    print("odd")

if b%2 == 0:
    print("even")
else:
    print("odd")

if c%2 == 0:
    print("even")
else:
    print("odd")

n = input()
n = int(n)

if n<0:
    if n%2==0:
        print("A")
    else:
        print("B")
else:
    if n%2==0:
        print("C")
    else:
        print("D")

n = input()
n = int(n)

if n >= 90:
    print('A')
else:
    if n >= 70:
        print('B')
    else:
        if n>= 40:
            print('C')
        else:
            print('D')

c = input()
if c == 'A':
    print("best!!!")
elif c == 'B':
    print("good!!")
elif c == 'C':
    print("run!")
elif c == 'D':
    print("slowly~")
else:
    print("what?")

# 왕개미 문제

