# 10992 별찍기

n = int(input())
print(" "*(n-1) +"*")
for i in range(2, n+1):
    if i == n:
        print('*'*((i*2)-1))
    else:
        print(" "*(n-i) +'*' + ' '* (2*(i-1)-1) + '*')