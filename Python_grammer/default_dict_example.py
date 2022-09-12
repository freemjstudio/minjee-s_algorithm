import collections


words = ["apple", "apple", "iphone", "mac", "mac", "mac"]
d_dict = collections.defaultdict(lambda: "hello") # int type으로 초기화
print(d_dict[1])
