# 첫번째 원소로 오름차순 정렬하기
v = [(3,4),(2,2),(3,3),(1,2),(1,-1)]
v.sort(key= lambda x:x[0])

# 첫번째 원소로 내림차순 정렬하기
# 1)
v.sort(key= lambda x:-x[0])
# 2)
v.sort(key = lambda x:x[0],reverse=True)

# 두번째 원소로 오름차순 정렬하기
v.sort(key=lambda  x:x[1])

# 첫번쨰 원소로 오름차순 정렬하고 첫번째 원소가 같은 경우 두번째 원소로 오름차순 정렬하기

v = [(3,4),(2,2),(3,3),(1,2),(1,-1)]
v.sort()

v.sort(key=lambda x:(x[0],x[1]))

# 첫번째 원소로 내림차순 정렬하고, 첫번째 원소가 같은경우 두번쨰 원소로 오름차순
v.sort(key=lambda x:(-x[0],x[1]))
