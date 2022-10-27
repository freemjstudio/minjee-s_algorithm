# 2417

n = int(input())
start = 0
end = n

while start <= end:
    mid = (start+end)//2
    if mid**2 < n:
        start = mid + 1
    else:
        end = mid - 1
# 탈출 조건에 의해서 start가 q**2 >= n 를 만족한다 ..
print(start)
