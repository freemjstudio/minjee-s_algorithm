# 2차원 배열 파이썬으로 하는 법
d = [] # 대괄호 [] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20):
    d.append([]) # 리스트 안에 다른 리스트 추가해 넣기
    for j in range(20):
        d[i].append(0) # 리스트 안에 들어있는 리스트 안에 0 추가해 넣기

#다른 방법
b = [[0 for j in range(20)] for i in range(20)]

# 입력값이 이차원 리스트인 경우 받는 법
board = []

for i in range(20): # 초기화를 해준다.
    board.append([])
    for j in range(20):
        board[i].append(0)

for i in range(19):
   a = input().split() #일차원 리스트
   for j in range(19):
       board[i+1][j+1] = int(a[j]) # 주의 ~~ i+1, j+1이다.