#함수: 코드를 모아놓은 묶음
# f(x) = x + 10
# input =>코드를 모아놓은 묶음 => output
# 파이썬 내장 함수
# print() 함수
# input() 함수
# int() 함수
# enumerate() 함수

# 파이썬 커스터마이즈 함수
# def add(x,y):
#     result = x+y
#     return result
# a = add(5,10)
# print(a)

# minus 함수
# def add(x,y):
#     return x-y
#
# b = add(4,11)
# print(b)

# multiply 함수

# def add(x,y):
#     return x * y
#
# c = add(4,11)
# print(c)

# 홀수 이면 홀수, 짝수이면 짝수라고 나오는 문자를 만들어보기

# def oddEven(x):
#     if x % 2 == 0:
#         return "짝수입니다."
#     else:
#         return "홀수입니다."


breads = ['소금빵', '보름달', '단팥빵', '앙버터','마카롱']
prices = [2500, 1000, 2400, 4500, 3000]

def makeListDict(xList,yList,xKey,yKey):
    return [{xKey:x, yKey:y} for x,y in zip(xList,yList)]

result = makeListDict(breads,prices,'빵','가격')
print(result)

# xKey값은 item, yKey값 price
def makeListDict(xList,yList,xKey='items',yKey='price'):
    return [{xKey: x, yKey:y} for x,y in zip(xList,yList)]
