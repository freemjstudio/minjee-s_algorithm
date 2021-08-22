#1676

N = int(input())

def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    result = str(result)
    count = 0
    length = len(result)-1
    for i in range(length, -1, -1):
        if result[i] == '0':
            count += 1
        else:
            print(count)
            break

factorial(N)