import pandas as pd

df = pd.read_csv('cgv.csv')
# 데이터프레임의 멤버 변수
# print(df.shape) # 행과 열의 수
# print(df.index) # 행 정보
# print(df.columns) # 열 정보
# print(df.values)  # 데이터
# 데이터프레임의 멤버 함수
# print(df.head(20)) # 위에서 20개 가져오기
# print(df.tail(20)) # 뒤에서 20개 가져오기
# print(df.describe()) # 전체 데이터 요약본

# group_by : 기준 잡기
# group_by_movies = df.groupby('moives') # 영화별로 그룹핑
# ages_group_by_movies = group_by_movies['ages'].value_counts() # 영화 기준으로 나이
# print(ages_group_by_movies)

# group_by_times = df.groupby('times')
# drinks_group_by_times = group_by_times['drinks'].value_counts()
# print(drinks_group_by_times)

# 나이대 별로 지불 그룹핑
# 영화 별로 스낵 그룹핑
# 시간대 별로 영화 그룹핑

# group_by_ages = df.groupby('ages')
# payments_group_by_ages = group_by_ages['payments'].value_counts()
# print(payments_group_by_ages)
#
# group_by_movies = df.groupby('movies')
# snacks_group_by_movies = group_by_movies['snacks'].value_counts()
# print(snacks_group_by_movies)
#
# group_by_times = df.groupby('times')
# movies_group_by_times = group_by_times('moives').values_counts()
# print(movies_group_by_times)


# 시간대 별로 가장 인기있는 영화
print(df.groupby('times')['movies'].value_counts())
popolar_movies = df.groupby('times')['movies'].value_counts().groupby(level=0).head(1)
print(popolar_movies)

# x대 별로 가장 인기 있는 y
def most_x_to_y(x,y):
    return df.groupby(x)[y].value_counts().groupby(level=0).head(1)

print(mosto_x_to_y('ages,'snacks'))