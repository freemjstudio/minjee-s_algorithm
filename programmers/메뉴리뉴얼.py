from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order), c)  # list
        count = Counter(temp)  # 조합 몇번 등장하는지 세기 ex) ('A', 'C') : 2
        if len(count) != 0 and max(count.values()) != 1:  # 주문이 2회이상이어야 한다
            for key, value in count.items():
                if value == max(count.values()):
                    answer += [''.join(key)]

    answer.sort()  # 오름차순으로 정렬
    return answer