#1085

x,y,w,h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

a = h-y
b = w-x
distance = [x,y,a,b]
# x,y,a,b중에서 최소값 구하기
result = min(distance)
print(result)