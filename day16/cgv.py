import pandas as pd
import random
from datetime import *
from faker import Faker

fake = Faker('ko_KR')

movieList = ['웡카','시민덕희','도그맨', '너의 이름은', '라라랜드', '상견니',' 외계인']
snackList = ['일반 팝콘','캬라멜 팝콘', '치즈 팝콘', '구운 오징어', '나초', '프레즐','핫도그']
drinkList = ['콜라','제로콜라','스프라이트','환타','에이드','물']


cgvData = {
    'customers':[fake.name() for i in range(500)],
    'movies':[random.choice(movieList) for i in range(500)],
    'movies':[random.choice(movieList) for i in range(500)],
    'snack':[random.choice(snackList) for i in range(500)],
    'drink':[random.choice(drinkList) for i in range(500)]
}

cgv_df = pd.DataFrame(cgvData)
now = datetime.now()
cgv_df.to_csv(f'0124 cgv_csv',index=False)