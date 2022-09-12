import re
import collections

text = "I want to buy iphone"
text_mod = re.sub('iphone', 'macbook', text)
print(text_mod)

text2 = "hello HELLO, my name is minjee. I woke up early today."
# 이 문장에서 , 라던가 . 를 제거
text2_mod = re.sub(r'[^\w]', ' ', text2)
words = [word for word in text2_mod.split()]
print(text2)
print(text2_mod)
print(words)

# 파이썬 정규표현식에서 \w : 문자열이라는 뜻
# ^ : not

array = collections.defaultdict(int)
print(array)
for word in words:
    array[word] += 1
print(array)

count = collections.Counter(words)
print(count)
print(count.most_common(1))
print(count.most_common(2)) # 두개까지 ..? 인듯
print(count.most_common(1)[0][1])
print(count.most_common(1)[0][0])