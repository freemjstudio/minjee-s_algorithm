t = int(input())  # test case
for i in range(t):
    n, s = input().split()
    n = int(n)
    text = ''
    for j in s:
        text += n*j
    print(text)

a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

