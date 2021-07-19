maze = [[]*10 for _ in range(10)]
for i in range(10):
    maze[i] = list(map(int, input().split()))
x = 1
y = 1

while True:
    if (maze[x][y]==2):
        maze[x][y]=9
        break
    if (maze[x][y+1] != 1):
        maze[x][y] = 9
        y += 1
    else:
        if (maze[x+1][y] != 1):
            maze[x][y] = 9
            x += 1
        else:
            maze[x][y] = 9
            break
        

for i in range(1,11):
    for j in range(1,11):
        print(maze[i][j], end=' ')
    print()





board=[[]*10 for _ in range(10)]
for i in range(10):
    board[i]=list(map(int,input().split()))
x=1
y=1
board[x][y]=9

while True:
    if(board[x][y]==2):
        board[x][y]=9
        break
    if(board[x][y+1]!=1):
        board[x][y]=9
        y+=1
    else:
        if(board[x+1][y]!=1):
            board[x][y]=9
            x+=1
        else:
          board[x][y]=9
          break

for i in range(10):
    for j in range(10):
        print(board[i][j],end=' ')
    print()