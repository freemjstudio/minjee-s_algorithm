#15666 N과 M(12)

n, m = map(int, input().split())
array = sorted(list(set(map(int, input().split()))))
temp = []

def solve(count):
    if count == m:
        print(" ".join(map(str, temp)))
        return
    for i in range(len(array)):
        if count == 0 or temp[-1] <= array[i]:
            temp.append(array[i])
            solve(count+1) # 여기서 재귀함수 호출
            temp.pop() # 맨 앞 원소를 바꿔줄 차례 !!

solve(0)
