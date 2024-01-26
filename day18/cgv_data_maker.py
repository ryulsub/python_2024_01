import pandas as pd
import random
from faker import Faker


faker = Faker('ko_KR')


# name, ages, genders, movie, payments, snack, drinks, times

ageList = [20, 30, 40, 50, 60]
agePercent = [30,30,20,15,5]
genderList = ['m','f']
movieList = ['웡카','시민덕희','도그맨','너의이름은','외계인']
moviePercent = [40,10,5,5,40]
paymentsList = ['현금','체크카드','신용카드','카카오페이','네이버페이']
paymentsPercent = [5,30,35,20,10]
snackList = ['선택 안함','일반팝콘','캬라멜팝콘','나초','오징어','맛밤']
snackPercent = [50,10,10,15,10,5]
drinkList = ['선택 안함', '콜라',' 제로 콜라', '물', '에이드', ' 스프라이트', '오렌지쥬스']
drinkPercent = [30,10,20,10,10,15,5]
timeList = ['조조',' 일반', '심야']
timePercent = [20, 70, 10]

data = {
    'name' : [faker.name() for i in range(500)],
    'ages' : [random.choices(ageList, weights=agePercent, k=1)[0] for i in range(500)],
    'genders': [genderList[random.randint(0,1)] for i in range(500)],
    'movies': [random.choices(movieList, weights=moviePercent, k=1)[0] for i in range(500)],
    'payments': [random.choices(paymentsList, weights=paymentsPercent, k=1)[0] for i in range(500)],
    'snacks': [random.choices(snackList, weights=snackPercent, k=1)[0] for i in range(500)],
    'drinks': [random.choices(drinkList, weights=drinkPercent, k=1)[0] for i in range(500)],
    'times': [random.choices(timeList, weights=timePercent, k=1)[0] for i in range(500)],
}
df = pd.DataFrame(data)
df.to_csv('cgv.csv',index=False)

