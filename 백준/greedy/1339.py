# 1399 단어 수학
import sys

n = int(sys.stdin.readline())
alpha = [] # 단어 저장
alpha_dict = {} # 알파벳 수 저장
num = []

for i in range(n):
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n):
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 이미 있으면
            alpha_dict[alpha[i][j]] += 10 **(len(alpha[i])-j-1)
        else:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

# value 만 추가한다
for val in alpha_dict.values():
    num.append(val)

num.sort(reverse=True) # 내림차순 정렬하기
pows = 9
sum = 0
for i in num:
    sum += pows * i
    pows -= 1
print(sum)