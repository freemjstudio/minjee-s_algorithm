# 20210 파일 탐색기

import re
from functools import cmp_to_key

array = []

n = int(input())

for i in range(n):
    data = input()
    temp = re.findall("[a-zA-Z]|\d+", data) # ['F', 'o', 'o', '12', 'B', 'a', 'r']
    array.append([data, temp])

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz" # 인덱스 반환을 위한 문자열 생성
# 사용자 정의 정렬 함수 -> sort 에서 이 함수를 기준으로 정렬한다
def comp(first, second):
    for i in range(min(len(first[1]), len(second[1]))):
        # first 숫자열 second 문자열인경우
        if first[1][i].isdigit() and second[1][i].isalpha():
            return -1 # first 가 앞에 나와야 함
        elif first[1][i].isalpha() and second[1][i].isdigit():
            return 1 # second가 왼쪽으로 가야함
        elif first[1][i].isdigit() and second[1][i].isdigit(): # 숫자열과 숫자열의 비교
            if int(first[1][i]) == int(second[1][i]):
                if len(first[1][i]) == len(second[1][i]):
                    continue
                return len(first[1][i]) - len(second[1][i]) # 0 개수 비교 -> 숫자 길이 비교
            else:
                return int(first[1][i]) - int(second[1][i])
        elif first[1][i].isalpha() and second[1][i].isalpha(): # 문자열 vs 문자열
            if first[1][i] == second[1][i]:
                continue
            else:
                return alphabet.index(first[1][i]) - alphabet.index(second[1][i])
    return len(first[1][i]) - len(second[1][i])

answer = sorted(array, key = cmp_to_key(comp))
for i in answer:
    print(i[0])



