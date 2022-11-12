def MathChallenge(strParam):
    def calc(x, y, op):
        if op == '+':
            return x + y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return x - y

    data = strParam.split()
    stack = []
    for i in data:
        if i.isdigit():
            stack.append(int(i))
        else:  # 연산자
            y = stack.pop()
            x = stack.pop()
            temp = calc(x, y, i)
            stack.append(temp)
    result = stack.pop()
    # code goes here
    return result


# keep this function call here
print(MathChallenge(input()))