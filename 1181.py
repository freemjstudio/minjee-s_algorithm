n = int(input()) # 단어의 개수
words = []
for i in range(n):
    words.append(input())

set_words = set(words)
words = list(set_words)
words.sort()
words.sort(key=len) # .. 이게 파이썬이다 헐

for i in words:
    print(i)
    