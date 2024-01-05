#산술 연산자[결과:숫자] +,-,*,/,//,%,**

# 100이하의 정수를 입력받고 10의자리와 1의 자리를 출력하는 프로그램 #ex) 89 -> 8,9
#num = int(input("정수 입력:")) #75
#ten = num // 10 #7
#one = num % 10 #5

# 1000이하 정수를 입력 받고 # 분 시로 환산하는 프로그램 # 72 -> 1분 12초
#time = int(input("정수 입력:"))
#minute = time // 60
#second = time % 60
#print(f"{minte}분 {second}초")

#정수: 10000~99999사이를 입력받고
#100의 자리값을 출력하는 프로그램
#ex) 17300 -> 3 / 93471 -> 4

num = int(input("1000~99999 사이의 정수 입력:"))
#45871 -> 458
hundred = num // 100 # 458 (백이하 자리 없애기)
result = hundred % 10 # 458 -> 8
print(result)


# 비교 연산자[결과:Bool]
# >, <, >=, <=, ==(같다), !=(다르다)
#a = 3 > 1 #bool type
#b = 3 == 1 #bool type [False]
#c = 3 !== 1 #bool type [Type]

# 논리 연산자[결과:bool]
# and: 피연산자가 모두 True이면 True
print(3 > 1 and 5 > 1) #True
# or: 피연산자가 하나라도 True이면 True
print(5 < 1 or 3 < 1 or 0 < 1) # True
# not: false -> true, true -> false
print(not(3 > 1)) # true -> false



# 할당 연산자
a = 1
a = 3 #3으로 갈아치우기
# a얼마? 3
b = 1
# b = b + 3 # 3을 더해주기
b += 3 # 3을 더해주기
b -= 3 # 3을 빼주기
b *= 3 # 3을 곱해주기
b /= 3 # 3을 나누기
