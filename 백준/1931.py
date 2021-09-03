# 1931 회의실 배정
import sys

N = int(sys.stdin.readline())
timetable = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    timetable.append([start,end])

timetable = sorted(timetable, key= lambda x:x[0])
timetable = sorted(timetable, key= lambda x:x[1]) # 끝나는 시간 순서대로 정렬하기 !!!
last = 0
count = 0
for start, end in timetable:
    if start >= last: #문제에 회의의 시작시간과 끝나는 시간이 같을 수도 있다고 적혀있음 ^^;; 
        count += 1
        last = end

print(count)