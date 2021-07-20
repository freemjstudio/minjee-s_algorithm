# 2869

a, b, v = map(int, input().split())
day = (v-b)/(a-b)
print(int(day) if day==int(day) else int(day)+1)

if day == int(day):
    print(day)
else:
    print(int(day)+1)

while True:
    day += 1
    if a*day-b*(day-1) >= v:
        break

print(day)

#-> 시간 초과

# 삼항 연산자


