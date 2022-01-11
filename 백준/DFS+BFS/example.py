from collections import deque

x = 1234
a = deque()
for i in str(x):
    a.append(i)
print(a)

a.insert(0, 1000)
print(a)


# tmp = a.popleft()
# print(a)
# a.append(tmp)
# print(a)




