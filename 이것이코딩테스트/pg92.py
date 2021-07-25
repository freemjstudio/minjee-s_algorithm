# 큰 수의 법칙
n,m,k = map(int, input().split()) # 첫 줄 입력받기 , n 개의 자연수가 입력된다.
data = list(map(int, input().split())) # 숫자 데이터 입력받기
data.sort() # 입력 받은 데이터를 오름차순으로 정렬한다.
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수


