# 1918 후위 표기식

data = input()
stack = []
result = ''

for now in data:
    if now.isalpha(): # 피연산자인 경우
        result += now   # 바로 결과로 출력해준다
    else:
        if now == '(':
            stack.append(now)
        elif now == '*' or now == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(now)

        elif now == '+' or now == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(now)

        else: # ')' 인 경우
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() # '(' 도 빼주어야 한다

while stack:
    result += stack.pop()
print(result)

