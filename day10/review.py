#1. 리스트 컴프리헨션을 이용한 짝수 생성
#[2, 4,6,8,10,12,14,16,18,20]
# [i for i in range(1,21) if i % 2 ==0]
# [i for i in range(2,21,2)]


#2. 조건을 포함한 리스트 컴프리헨션 [1,2,3,4,5,6,7,8,9,10]
# numList = [1,2,3,4,5,6,7,8,9,10]
# overFiveList = [i for i in numList if i > 5]


#3. 문자열 처리를 위한 리스트 컴프리헨션 ["apple","banana","cherry","date"]
 fruits = ["apple", "banana", "cherry", "date"]
# fristLetters = [i[0] for i in fruits]

#4. 4번 문제 대문자화

fruitsUppers = [i.upper() for i in fruits]