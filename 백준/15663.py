from itertools import permutations

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
permu = list(permutations(array, m))
result = []

for p in permu:
    result.append(p)
result = sorted(list(set(result))) # set 을 통해 중복 제거한다 !

for r in result:
    for i in r:
        print(i, end=' ')
    print()
