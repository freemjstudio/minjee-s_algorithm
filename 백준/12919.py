# 12919 A와 B 2
import sys
input = sys.stdin.readline
s = input()
t = input()
flag = False
n = len(t)
def change(word, n):
    global flag
    if len(word) == n:
        if word == t:
            flag = True
        return
    # A 를 추가하는 경우
    change(word+'A', n)
    # B를 추가하는 경우
    temp = word+'B'
    change(temp[::-1], n)

change(s, n)
if flag:
    print(1)
else:
    print(0)