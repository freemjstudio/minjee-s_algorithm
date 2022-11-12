from collections import defaultdict


def solution(gems):
    n = len(set(gems))  # 보석 종류
    shortest = int(1e9)
    left = 0
    right = 1
    if n == 1:
        return [1, 1]
    else:
        for i in range(len(gems)):
            temp = defaultdict(int)
            temp[gems[i]] = 1
            for j in range(i + 1, len(gems)):
                if gems[j] in temp:
                    continue
                else:
                    temp[gems[j]] = 1
                    if len(temp) == n:
                        if shortest > (j - i + 1):
                            shortest = j - i + 1
                            left = i
                            right = j

        return [left + 1, right + 1]