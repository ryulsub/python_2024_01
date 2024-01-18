# lambda
# 간결하고 이름이 없는 한 줄 함수

#def add(a,b):
#    return a+b 할거를 밑에 lambda로

# plus = lambda a, b: a + b
# result = plus(5,7)
# print(result)
#
# minus = lambda a, b:a - b
# result = minus(5,7)
# print(result)
#
# multi = lambda a, b:a * b
# result = multi(5,7)
# print(result)






# callback 함수
# something(add)
# something(add(3,5))

def hello(some):
    print("안녕!")
    some()

def bye():
    print('잘가')
hello(bye)


eggs = ['🥚''🥚''🥚']

def cookEggs(eggs,index,recipe):
    recipe(eggs,index)

def makeFry(eggs,index):
    eggs[index] = '🍳'

def makeSandwich(eggs, index):
    eggs[index] = '🥪'

cookEggs(eggs,0,makeFry)
cookEggs(eggs,1,makeSandwich)
print(eggs)