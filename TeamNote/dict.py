# dictionary
dic = {'apple':1, 'banana':3}
dic['plus'] = 5

del dic['apple']
print(dic.keys()) # keys() 는 key 만을 모아서 dict_keys 객체를 돌려준다
print(dic.get('plus', 0)) # get : key로 value 얻는 함수
# 0 은 현재 가져오려는 Key 값이 딕셔너리 안에 없을 경우 디폴트값을 대신 가져오게 한다.