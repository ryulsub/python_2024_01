# pandas
# 엑셀을 파이썬화
# 판다스 데이터 타입: series, dataframe
# series: 엑셀에서 하나의 열
# dataframe: 엑셀 그 자체[스프레드시트]

import pandas as pd
from faker import Faker

#numList = [5, 12, 24, 13, 17]
#series = pd.Series(numList)
#series.apply()

# coffeeList = ['아아','라떼','바닐라','모카','초코']
# series = pd.Series(coffeeList)
# print(series)

# coffeeData = {
#     "menu":['americano','latte','mocha','vallina','mint'],
#     "price": [2500, 3000, 3500, 3500, 4000],
#     "caffeine": [120, 100, 80, 100, 50],
# }
#
# df = pd.DataFrame(coffeeData)
# df.to_csv('coffee.csv', index=False)

fake = Faker()
#print(fake.name())

fake = Faker('ko_KR')
carData = {
     'carName': ['k5','k7','avante','genesis','tesla'],
     'owner':[fake.name() for i in range(5)],
}
df = pd.DataFrame(carData)
df.to_csv('car.csv',index=False)


