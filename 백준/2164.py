import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque([i+1 for i in range(n)])


while len(cards) > 1:
    cards.popleft()
    temp = cards.popleft()
    cards.append(temp)
print(cards[0])


input = int(input())
square = 2

while True:
    if (input == 1):
        print(input)
        break
        square *= 2
    if (square >= input):
        print((input - (square/2))*2)
        break

n = int(input())
s = 2

while True:
    if (n == 1 or n == 2):
        print(n)
        break
    s *= 2
    if (s >= n):
        print((n - (s//2))*2)
        break