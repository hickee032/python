# dictionary 딕셔너리
# 키와 값이 쌍으로 존재하는 형태
# {키 : 값}
# 첫번째 키 값이 문자열이면 두번째 키 값도 문자이어야 한다.

dic = {'애플': 'apple', '파이썬': 'python', '마이크로소프트': 'micro', '구글': 'google'}
for key, value in dic.items():
    print(f'키 : {key}, 값 : {value}')

# 키 검색 1
key = '구글'
if key in dic.keys():
    print(f'key {key} 가 딕셔너리에 있습니다.')
else:
    print(f'key {key} 가 딕셔너리에 없습니다.')

key = '파이썬'
if key in dic.keys():
    print(f'key {key} 가 딕셔너리에 있습니다.')
else:
    print(f'key {key} 가 딕셔너리에 없습니다.')

# 키 검색 2
find_key = '애플'
res = dic.get(find_key)
print('키를 검색해서 value 값을 리턴 : ', res)
# 없다면 None

# 삭제
del dic['마이크로소프트']
print('삭제 후 딕셔너리 ', dic)

# 값 검색
value = 'apple'
if value in dic.values():
    print(f'value {value} 가 딕셔너리에 있습니다.')
else:
    print(f'value {value} 가 딕셔너리에 없습니다.')
# 추가
dic['삼성전자'] = 'samsung'

# 연습
strKey = input('키 값을 입력 : ')
if dic.get(strKey) is None:
    print(f'key {strKey} 가 딕셔너리에 없습니다.')
    dic[strKey] = 'samsung'
else:
    del dic[strKey]
    print(f'key {strKey} 가 딕셔너리에서 삭제했습니다.')
print('결과', dic)
