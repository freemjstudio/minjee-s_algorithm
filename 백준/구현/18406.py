# 문자열 재정렬
data = input()

word = []
number = 0
for i in data:
    if i.isalpha():
        word += i
    else:
        number += int(i)
word.sort()

if number != 0:
    word.append(str(number))

print(''.join(word))