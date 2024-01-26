import pandas as pd
# apply: 새로운 열을 만들기

df = pd.read_csv('cgv.csv')

def recommendPopcornForSenior(row):
    if row['ages'] == 50 and row['snacks'] == '일반 팝콘':
        return '할인 대상'
    else:
        return '할인 없음'
df['50대 할인 이벤트'] = df.apply(recommendPopcornForSenior,axis=1)
print(df)

# 조조이고 체크카드 사용하면 조조이벤트 해당됨, 해당안됨

def morningEvent(row):
    if row['time'] == '조조' and row['payments'] == '체크카드':
        return '해당됨'
    else:
        return '해당 안됨'
df['조조 이벤트'] = df.apply(morningEvent, axis=1)

def comboEvent(row):
    if row['snack'] == '일반 팝콘' and row['drinks'] == '제로 콜리':
        return '제로콤보 세트'
    else:
        return ' 해당 없음'

df['제로 이벤트'] = df.apply(comboEvent, axis=1)

print(df.head(200))
