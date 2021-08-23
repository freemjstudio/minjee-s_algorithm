N, M = map(int, input().split())

hear = set()
see = set()

for i in range(N):
    hear.add(input())
for i in range(M):
    see.add(input())
result = hear & see
result = list(result)
result.sort()
print(len(result))

for i in result:
    print(i)