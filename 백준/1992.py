# 1992 쿼드 트리

N = int(input()) # N 은 언제나 2의 제곱수이다.
 image = [list(map(int,input())) for _ in range(N)]

def quadtree(x, y, n):
    if (n == 1):
        return str(image[x][y])
    result = []

    for i in range(x,x+n):
        for j in range(y,y+n):
            if (image[i][j] != image[x][y]): # pixel의 색이 다른경우
                result.append("(")
                result.extend(quadtree(x,y,n//2))
                result.extend(quadtree(x,y+n//2,n//2))
                result.extend(quadtree(x+n//2,y,n//2))
                result.extend(quadtree(x+n//2,y+n//2,n//2))
                result.append(")")

                return result
    return str(image[x][y])




# result
print("".join(quadtree(0,0,N)))