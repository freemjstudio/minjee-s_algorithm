# 1620

N,M = map(int,input().split())
pokemon = {}

for i in range(N):
    name = input()
    i += 1
    i = str(i)
    pokemon[i] = name

pokemon2 = {v:k for k,v in pokemon.items()}
for i in range(M):
    temp = input()
    if temp.isdigit():
        print(pokemon[temp])
    else:
        print(pokemon2[temp])