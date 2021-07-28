#1920 수 찾기

n = int(input())
numbers = list(map(int, input().split()))

m = int(input())
finders = list(map(int, input().split()))

for i in finders:
    if i in numbers:
        print("1")
    else:
        print("0")

# 이렇게 풀이하면 시간초과가 난다.. 백준은 시간초과 날때 보통 내장 함수를 써서 나는 경우가 많은 것 같다.
# 편리하지만 그만큼 연산량이 늘어나는거지 ~ 무야호

