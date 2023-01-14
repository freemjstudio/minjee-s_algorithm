num = [1,2,3]
alphabet = ["a", "b", "c"]

for pair in zip(num, alphabet):
    print(pair)
# OUTPUT
# (1, 'a')
# (2, 'b')
# (3, 'c')

print(dict(zip(num, alphabet)))
# {1: 'a', 2: 'b', 3: 'c'}
