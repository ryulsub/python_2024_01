# Pandas를 활용한 데이터 분석
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv ('bicycle.csv', encoding='cp949')

def dong(row):
    if row['시작_대여소명']:
        return row['시작_대여소명'].split('_')[0]

def changeTime(row):
    if row['기준_시간대'] or row['기준_시간대'] == 0:
        time = row['기준_시간대']
        if 0 <= time and time < 500:
            return "새벽"
        elif 500 <= time and time < 1000:
            return "아침"
        elif 1000 <= time and time < 1600:
            return "점심"
        elif 1600 <= time and time < 2000:
            return "저녁"
        else:
            return "밤"

df['가공된_대여소명'] = df.apply(dong, axis=1)
df['가공된_시간'] = df.apply(changeTime, axis=1)
times_groupby_places = df.groupby('가공된_대여소명')['가공된_시간'].value_counts()

sinchon_data = times_groupby_places['신촌동']

plt.rcParams['font.family'] = 'Malgun Gothic'
sinchon_data.plot(kind='pie', autopct = '%1.1f%%')
plt.show()
