# map(어떻게, 무엇을) - 변경/ 치환해주는 함수

# numList = [1, 2, 3, 4, 5]
#
# # def square(x):
# #     return x**2
# a = map(lambda x: x**2, numList)
# b = map(lambda x: x+100,numList)
# c = map(lambda x: x**2+100,numList)
# print(list(a))
# print(list(b))
# print(list(c))

# coffeePriceList = [2000, 3000, 3500, 4000]
# # '3000원' , '4000원', '3500원', '5000원'
#
# d = map(lambda x: str(x+1000)+'원' , coffeePriceList)
# print(list(d))

# fruits = ['apple', 'banana', 'mango', 'avocado']
# # 5 6 5 7
# e = map(lambda x: len(x),(fruits)





# filter (어떻게, 무엇을) 컷/필터

# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter(lambda x: x > 5,numList)

#
# filter(lambda x: x % 2 == 0,numList)



fruits = ['apple', 'banana', 'mango', 'avocado']
# filter(lambda x: 'o' in x,fruits)


# 6글자 이상인 애들만 걸러 주고, '🐱 banana', '🐱 avocado'
a = filter(lambda x: len(x) > 5 ,fruits) # 6글자
b = map(lambda x: "🐱"+x,a)

print(list(map(lambda x: "🐱"+x, filter(lambda x: len(x) > 5, fruits))))
print(list(b))