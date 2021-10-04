# 1107 리모컨

numbers = {str(i) for i in range(10)} # 입력 불가능한 번호들을 제거해주기 위해서 set으로 선언한다

N = int(input()) # 이동하려는 채널
M = int(input()) # 고장난 버튼의 개수호
if M != 0:
    numbers -= set(map(str, input().split())) # 입력 불가능한 숫자들을 제외시킨다.

start = 100
count = abs(start - N) # 입력횟수를 저장하는 변수를 최대의 경우로 선언함

for i in range(1000000):
    for j in range(len(str(i))): # 현재 순회중인 채널의 각 자릿수를 조회
        if str(i)[j] not in numbers:
            break
        elif j == len(str(i)) - 1:
            count = min(count, abs(i - N) + len(str(i)))



print(count)