# 15829

L = int(input()) # 문자열의 길이
string = input() # 문자열 입력받기
hash = 0

for i in range(L):
    hash += (ord(string[i]) - 96) * (31 ** i)
print(hash % 1234567891)