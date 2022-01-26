# 배열 합치기

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a+b
answer = ' '.join(map(str, sorted(c))) # 반복문 대신 join으로 출력하기 !
print(answer)