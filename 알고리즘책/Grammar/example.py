data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['포도'] = 'grapes'

print(data)

if '사과' in data:
    print('YES')

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(key)