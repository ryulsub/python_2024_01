#for_comp(심화/축약 버전)

# a= []
# for i in range(1001):
#     a.append(i)

# a = [i for i in range(1001)]
#1. 0 ~ 100
#2. 1 ~ 500
# a = [i for i in range(1001)]
# b = [i for i in range(101)]
# c = [i for i in range(1, 501)]
# d = [i for i in "megastudy"]
# print(d)

# e = [i*2 for i in range(1,101)]

# 1. 1~10을 각각 제곱한 수의 리스트
# f = [i**2 for i in range(1,11)]
#
# # 2. 1~10에 각각 5를 더한 수의 리스트
# g = [i+5 for i in range(1,11)]



# for 컴프리헨션 조건문
# 1. if가 뒤에 있을 때는 filter 컷 역할
# [i for i in range(1,101) if i % 5 == 0]
# fruits = ['apple','strawberry','mango', 'orange', 'melon']
# a = [i for i in fruits if i.count('a') > 0] # 'a' 하나 이상 포함
# b = [i for i in fruits if i.count('r') == 1] # 'r'이 하나만 포함
# c = [i for i in fruits if len(i) >= 6] # 6글자 이상인 단어들
# print(c)

# 2. if - else 있을 때는 map 변환 역할
#2. if - else   # [i % 2 == (짝수라는뜻)]

# a= ['🍓' if i % 2 == 0 else i for i in range(1,101)]
# print(a)

# 1. 유저에게 n을 입력 받고, 1~100까지 리스트를 출력을 하는데,
# n의 배수만 '🥕'을 표현해주고 나머지는 숫자로 표현

# num = int(input("정수 입력:"))
# b = ['🥕' if i % num == 0 else i for i in range(1,101)]
# print(b)

# 2. fruits = ['apple','strawberry','mango', 'orange', 'melon']
# fruits에서 5글자 이하이면 대문자로 바꿔서 출력하고
# 아니면 🐇로 출력하는 리스트 만들기

# fruits = ['apple','strawberry','mango', 'orange', 'melon']
# c = [i.upper() if len(i) <= 5 else '🐇' for i in fruits]
# print(c)


# for 컴프리헨션 중첩 루프문

h = [i*j for i in range(1,3) for j in range(1,3)]
g = [i for i in ["apple", "banana"] for j in ["pie","tanghuru"]]
print(g)
# i - 1 j - 1,2
# i - 2 j - 1,2

