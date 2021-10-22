s = input()
num = ['0','1','2','3','4','5','6','7','8','9']
score = 0
abc = []

for i in s:
    if i in num:
        score += int(i)
    else:
        abc.append(i)

abc.sort()

print(''.join(abc),score)

# 다른 풀이

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()


# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입 !!!! 
if value != 0:
    result.append(str(value))

print(''.join(result))