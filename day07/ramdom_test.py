#random_test
import random

fruits = ['사과','망고','바나나']

print(random.randint(0,100))
print(random.random()) # 0~1 실수
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)
