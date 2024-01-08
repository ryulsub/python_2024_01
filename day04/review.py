# 1. 정삼각형의 넓이와 둘레를 계산하는 프로그램 문구
# "사용자로부터 밑변과 높이를 입력받아 정삼각형의 넓이와 둘레를 구하는 프로그램"

height = int(input("높이 입력:"))
side = int(input("한변의 길이 입력:"))
print(f"정삼각형의 넓이는 {height+side*0.5} 둘레는 {side*3}")

#2. 운동 순서 만들기 프로그램
#"사용자로부터 원하는 운동 종류를 3개 입력받아, 이를 바탕으로 효과적인 운동 순서를 생성하는 프로그램을 만들어보세요!
#운동 입력 : 스트레칭, 윗몸일으키기, 운동 입력:러닝 '운동순서:스트레칭 ->

a = input("운동 입력")
b = input("운동 입력")
c = input("운동 입력")
print(f":운동 순서:{a}->{b}->{c}")

movieList = ['서울의 봄', '위시', '노랑']
popcornList = ['일반 팝콘', '치즈 팝콘', '캬라멜 팝콘']
drinkList = ['콜라', '제로 콜라', '스프라이트']

#영화 리스트,팝콘
movie = int(input("영화 번호 고르시오[1번: 서울의 봄 2번: 위시 3번: 노랑]:")) - 1
popcorn = int(input("팝콘 번호 고르시오[1번: 팝콘 2번: 치즈 팝콘 번: 카라멜팝콘]:")) - 1
drink = int(input("음료 번호 고르시오[1번: 콜라 2번:제로콜라 팝콘")) - 1
print(f" 고르신 영화는 {movieList[movie]}이며 팝콘은 {popcornList[popcorn]} 그리고 음료는 {drinkList[drink]} 주문하셨습니다!")
# print(movieList[movie - 1])