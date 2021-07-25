#1157

word = input().upper()
unique_word = list(set(word))
count_list = []

for i in unique_word:
    cnt = word.count(i)
    count_list.append(cnt)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_index = count_list.index(max(count_list))
    print(unique_word[max_index])

