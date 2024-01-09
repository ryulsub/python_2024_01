#list_advance

# 리스트 연산자
# + 연산자
# +: int + int(사칙 연산)
# +: str + str(문자 연결 연산)
# +: list + list(리스트 연결 연산)
# coffee = ['아메리카노', '라떼', '바닐라라떼']
# cookie = ['화이트 쿠키','녹차 쿠키', '오레오 쿠키']
# menu = coffee + cookie
# print(menu)

# * 연산자
# *: int * int (사칙연산)
# *: str * int (str을 n번 반복)
# *: list * int (list를 n번 반복)
# double_menu = menu * 2
# print(double_menu)

# in 연산자: boolean 타입 변환
# print('디카페인' in menu)

# [:] 슬라이싱 연산자:
# new_menu = menu[1:4]
# print(new_menu)


# 리스트 기능
# 1.리스트의 길이 기능:len()
store = ['cu','gs','seven','ministop']
print(len(store))
#2.리스트 추가[맨뒤]: append(무엇을)
store.append('emart24')
print(store)
#3. 리스트 추가[몇번째]: insert(몇번째,무엇을)
store.insert(2,'familtMart')
# print(store)

# 4. 리스트 제거: remove(무엇을)
store.remove('cu')
print(store)

# 5. 리스트 해당 아이템 위치 찾기: index(무엇을)
print(store.index('ministop'))

# 6. 리스트에 해당 아이템 몇개 세기: count(무엇을)
print (store.count('emart24'))

# 7.리스트를 추가: extend(리스트) +[같은역할]
newStore = ['storyway', 'buytheway']
store.extend(newStore)
print(store)

# 8. 리스트 정렬: sort() / sort(Reverse=True)
store.sort()
print(store)
store.sort(reverse=True)
