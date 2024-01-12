#1. 각도 프로그램

# 예각 - (0º ~ 90º미만)
# 직각 - 90º
# 둔각 - (90º초과 ~ 180º 미만)

# angle = int(input("각도 입력:"))
#
# if 0 < angle and angle < 90:
#     print('예각입니다.')
# elif angle == 90:
#     print("직각입니다.")
# elif 90 < angle and angle < 180:
#     print("둔각입니다.")
# elif angle == 180:
#     print("평각입니다.")
# else:
#     print("오바각")


#2. 테마파크 프로그램

#1. 일반 입장권 - 50000원
#2. 프리미엄 입장권(모든 놀이기구 무제한 이용) -75000원
#3. vip 입장권(모든 놀이기구 무제한 이용) - 100000원

# themapark = {
#     1.{
#         'ticketName' : '일반입장권',
#          'ticketprice'  : 50000,
#     },
#     2.{
#          'ticketName' : '프리미엄 입장권',
#          'ticketprice':  75000,
#          },
#     3.{ 'ticketName' : 'vip 입장권',
#          'ticketiprice': 100000,
#   },
# }
#
# ticket = int(input({["입장권을 고르세요"]["1.일반입장권" "2.프리미엄 입장권" "3.vip입장권"]
# age = int(input("나이를 입력하세요"))
#
# if age < 12:
#      print(f"선택하신 티켓은 {themapark[ticket]['ticketName']}이고, 가격은{themapark[ticket]['ticketprice']*0.5}입니다. ")
# elif 65 <= age:
#     print(f"선택하신 티켓은 {themapark[ticket]['ticketName']}이고, 가격은{themapark[ticket]['ticketprice']*0.7}입니다. ")
# else:print(f"선택하신 티켓은 {themapark[ticket]['ticketName']}이고, 가격은{themapark[ticket]['ticketprice']}입니다. ")
# }
#




#3.

import random

num = []
for i in range(6):
   x = random.randit(0,10001)
   num.append(x)
num.sort()
print(num)