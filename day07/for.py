# print, input, 변수, 데이터타입[int,float,str,bool,list,set,dict]
# if문,random,연산자,

# 컴퓨터 = 기억[RAM] + 연산[CPU]
# RAM : 변수[데이터 타입] , Ramdom
# CPU: 연산자, 명령문(print(), input(), len(), ~~()) , 조건문[if], 반복문[for]
#num = int(input("몇번 까지 보실래요?")) + 1
#for x in range(num):
  #  if x % 2 == 0:
       # print(x)
#print("끝")



# 유저한테 어떤정수를 입력받고, 그 수의 해당 공배수를 나오게

#num = int(input("공배수 입력:"))
#for x in range(1001):
 #   if x % num == 0:
  #      print(x)
#print("끝")


# 1~10까지의 총합을 구하는 프로그램

#sum = 0
#for x in range(11):
 #       sum += x
#print(sum)

# 유저에게 n의 정수를 받고, m의 정수를 받으면
# 0 ~ n 까지의 m의 공배수의 총합을 나타내는 프로그램

#n = int(input("몇번째 까지:"))
#m = int(input("공배수:"))
#sum = 0
#for x in range(n):
  #  if x % m == 0:
    #    sum += x
#print(f"총합:{sum}")


#for x in range(n):  # 0 ~ n - 1
#    print(x)
#for x in range(2,10):  # n ~ m - 1
#    print(x)


# ramdom, list, for
# 0~10000까지의 랜덤한 숫자를 담고 있는 리스트 출력
# [n,m,l,o,p,q]
number: [0,10000]
n = int(input("숫자 입력:"))
for x in range(0,1001):
    print(random.randit())
    print(x)



