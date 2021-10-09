# 21276

N = int(input())
array = list(input().split()) # 현재 살고 있는 마을 사람들의 이름
M = int(input()) # 기억하는 정보의 수
array.sort() # 마을 사람들 사전순으로 정렬하기 !
people_dict = []

for i in range(M):
    child, parent = input().split() # 자식, 부모



