n = input().rstrip()

temp1 = 0
temp2 = 0

for i in n[:len(n)//2]:
    temp1 += int(i)

for i in n[len(n)//2:]:
    temp2 += int(i)

if temp1 == temp2:
    print('LUCKY')
else:
    print('READY')

