#function_part2

# def add(x, y):
#     return x+y
#
# # 가변 매개 변수
#
# def makePizza(*toppings):
#     print("다음 피자는 아래의 토핑이 들어갑니다.")
#     for i in toppings:
#         print(i)
# makePizza("pineapple")
# makePizza("pineapple","cheese")
# makePizza("pineapple",'cheese', "mushroom")



#['닭',돼지','소']= zodiac(1993,1995,1997)
# 1993 ~ 2005 닭~닭
#['닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠', '용띠','뱀띠','말띠','양띠']

def zodiac(*years):
    sign = ['닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠', '용띠','뱀띠','말띠','양띠']
    return [sign[i - 1993] for i in years]

a = zodiac(1993,1994,1999,2002)
print(a)


