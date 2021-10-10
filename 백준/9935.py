
string = input() # 문자열 입력받기
bomb = input() # 폭발 문자열
lastChar = bomb[-1]
stack = []
length = len(bomb)

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)



if answer == '':
    print("FRULA")
else:
    print(answer)