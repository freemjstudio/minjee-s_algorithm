import re
import collections

text = "hello HELLO, my name is minjee. I woke up early today."
text_mod = re.sub(r'[^\w]', ' ', text)

#
# words = [word for word in text_mod.split()]
#
# array = collections.defaultdict(int) # int type으로 초기화
# print(array)
# for word in words:
#     array[word] += 1
# print(array)
#
# count = collections.Counter(words)
# print(count)
# print(count.most_common(1))
# print(count.most_common(2)) # 두개까지 ..? 인듯
# print(count.most_common(1)[0][1])
# print(count.most_common(1)[0][0])