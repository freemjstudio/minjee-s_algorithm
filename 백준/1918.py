# 1918 후위 표기식

data = input()
stack = []
op = []
i = 0


while True:
    if i == len(data):
        break
    if data[i].isalpha():
        stack.append(data[i])
    else: # 연산자
        if data[i] == '/' or data[i] == '*':
            if data[i+1].isalpha():
                stack.append(data[i+1])
                stack.append(data[i])
                stack.extend(op)
                op = []
                i += 1
            else:
                stack.append(data[i])
                stack.extend(op)
                op = []
        else:
            op.append(data[i])
    i += 1


for i in stack:
    print(i, end="")
