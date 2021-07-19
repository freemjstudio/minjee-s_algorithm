n = int(input()) # 입력값
sum = 0
c = 1
while True:
    sum += c
    if sum >= n:
        break
    c += 1
print(sum)

n = int(input()) # 입력한 수
for i in range (1, n+1):
    if i%3==0:
        continue
    print(i, end=' ')

a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

a = a + d*(n-1)
print(a)

a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

a = a * r **(n-1)
print(a)

a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1,n):
    a = a*m+d

#출력
print(a)

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1
print(d)

n = int(input()) # 개수를 입력받아 n에 정수로 저
a = input().split() #공백을 기준으로 잘라 a에 순서대로 저장
for i in range(n): #0 부터 n-1까지
    a[i] = int(a[i]) # a에 순서대로 저장되어 있는 각 값을 정수로 변환해서 다시 저

d = [] # d라는 이름의 빈 리스트 변수
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1


n = int(input()) # 번호를 부른 횟수
k = input().split()
for i in range(n):
    k[i] = int(k[i])

min = k[i]

for i in range(n):
    if min > k[i]:
        min = k[i]
    i += 1
print(min)


board = [] # 대괄호를 이용해 빈 리스트 만들기

for i in range(20):
    board.append([])
    for j in range(20):
        k = int(input()).split()
        board[i].append(int(k))

n = int(input()) # 바둑돌의 개수
#좌표값 입력 받기
for i in range(n):
    x, y = input().split()
    #바둑판 바꾸기
    board[int(x)][int(y)] = 1

for i in range(1,20):
    for j in range(1,20):
        print(board[i][j], end= ' ')
    print()



board = []

for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

for i in range(19):
   a = input().split() #일차원 리스트
   for j in range(19):
       board[i+1][j+1] = int(a[j]) # 인덱스 i,j는 한줄씩 밀린다 왜냐면 편의상 위에서 20*20로 만들었으니까

n = int(input()) # n 개의 좌표 입력 받기

for i in range(n):
    x,y = input().split()
    for j in range(1,20):
        if board[j][int(y)] == 0:
            board[j][int(y)] = 1
        else:
            board[j][int(y)] = 0

        if board[int(x)][j] == 0:
            board[int(x)][j] = 1
        else:
            board[int(x)][j] = 0

for i in range(1,20):
    for j in range(1,20):
        print(board[i][j], end=' ')
    print()

# 6097
board = []

h, w = input().split() # 세로 : h, 가로 : w
h = int(h) #5
w = int(w) #5
for i in range(h):
    board.append([])
    for j in range(w):
        board[i].append(0)

n = int(input()) #막대의 개수 #3

for i in range(n):
    l, d, x, y = input().split() # 길이, 방향, 좌표(x,y) n 번 입력 된다.
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    if d == 0: # 가로일때
        board[x-1][y-1] = 1
        for j in range(l-1):
            y += 1
            board[x-1][y-1] = 1
    else:
        board[x-1][y-1] = 1
        for k in range(l-1):
            x = x+1
            board[x-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end=" ")
    print()















