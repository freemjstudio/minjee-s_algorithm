# 17626 four squares

N = int(input())

def four_squares(N):
    temp = N**0.5
    if temp.is_integer():
        return 1
    for i in range(1, int(N**0.5)+1):
        if N < i**2:
            break
        if ((N - i **2)**0.5).is_integer():
            return 2
    for i in range(1, int(N**0.5)+1):
        if N < i**2:
            break
        for j in range(1, int((N - i**2)**0.5)+1):
            if N < i**2 + j**2:
                break
            if ((N - i**2 - j**2)** 0.5).is_integer():
                return 3
    return 4

print(four_squares(N))