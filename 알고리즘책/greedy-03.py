data = input()

count0 = 0 # 모두 0으로 바꾸는 경우
count1 = 0 # 모두 1로 바꾸는 경우

# 첫번쨰 원소에 대해서 처리하기

if data[0] == '1': # 첫번쨰 원소가 1인경우 
    count0 += 1
else: # 첫번쨰 원소가 0 인 경우 !!!!!
    count1 += 1

# 두번째 원소부터 모든 원소를 확인
for i in range(len(data) -1):
    if data[i] != data[i+1]:
        if data[i+1] == '1': # 다음수에서 1로 바뀌는 경우
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))