# 1918 후위 표기식

data = input()
stack = []
result = ''

for now in data:
    if now.isalpha():
        result += now
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
        else: # ')'
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()


while stack:
    result += stack.pop()

print(result)