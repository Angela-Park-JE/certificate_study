# 617 JungEun : 230620 TUE mission 32 (1)
# T1-1. 종량제 봉투 종류가 '규격봉투'이고, 종량제 봉투 용도가 '음식물쓰레기', 2L 가격 평균 
# 가격 0은 제외하고, 반올림 후 '정수'로 출력

# 1. 데이터, 라이브러리
import numpy as np
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0620 - 미션32/5-1price.csv')



# 2. conditions
cond1 = df['종량제봉투종류'] == '규격봉투'
cond2 = df['종량제봉투용도'] == '음식물쓰레기'
cond3 = df['2ℓ가격'] != 0



# 3. price
avg = df[cond1&cond2&cond3]['2ℓ가격'].mean()
print(int(round(avg)))


# 118
# 4분



# 복습 230913
"""
# 1 번
# 1. data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0620 - 미션32/5-1price.csv')

# 2. condition
data = df[(df['종량제봉투종류'] == '규격봉투')&(df['종량제봉투용도'] == '음식물쓰레기')&(df['2ℓ가격'] != 0)]['2ℓ가격']

# 3. isna() false's mean and round it
answer = round(data.mean())

print(answer) # 118
"""
