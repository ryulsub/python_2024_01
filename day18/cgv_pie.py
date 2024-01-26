# 일변량 그래프
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cgv.csv')
snacks_by_times = df.groupby('times')['snacks'].value_counts()
normal_time_snack = snacks_by_times[' 일반']

plt.rcParams['font.family'] = 'Malgun Gothic' # 폰트설정
normal_time_snack.plot.pie(autopct='%1.1f%%') # plot.pie() 파이그래프, autopct = 소수점자리
plt.show() # 보여주기

df = pd.read_csv('cgv.csv')
snacks_by_times = df.groupby('movies')['drinks'].value_counts()
normal_time_snack = snacks_by_times['웡카']

plt.rcParams['font.family'] = 'Malgun Gothic' # 폰트설정
normal_time_snack.plot.pie(autopct='%1.1f%%') # plot.pie() 파이그래프, autopct = 소수점자리
plt.show() # 보여주기
