#1. 홀수? 짝수? 확인해보세요!

# number = int(input("정수 입력:"))
# if number %2 == 0:
#     print("짝수 입니다.")
# else :
#     print("홀수 입니다.")

#2. 알파벳 탐지기!

# alpha = input("글자 입력:")
# if alpha.isalpha():
#     print("알파벳입니다😊.")
# else:
#     print("알파벳이아닙니다🤣.")

#3.비밀번호 설정 프로그램
#다시!!!!

#4. 버스 요금 계산기
# 1. 시내버스 - 1200원
# 2. 광역버스 - 2000원
# 3. 마을버스 - 1000원

bus = {
    1:{
        'name': '시내버스',
        'price': 1200,
    },
    2: {
        'name': '광역버스',
        'price': 2000,
    },
    3: {
        'name': '마을버스',
        'price': 1000,
},
}

bus_choice = int(input(f'버스를 선택하세요![1.시내버스 - 1200원, 2.광역버스 - 2000원, 3.마을버스 - 1000원]:')) - 1
age = int(input("나이를 입력하세요:"))

if age <= 7 or 65 <= age:
    print("무료 입니다!")
elif 8 <= age and age <= 19:
    print(f"{bus[bus_choice]['name']}의{bus[bus_choice]['price']*0.7}가격 입니다.")
else:
    print(f"{bus[bus_choice]['name']}의{bus[bus_choice]['price']}가격 입니다.")