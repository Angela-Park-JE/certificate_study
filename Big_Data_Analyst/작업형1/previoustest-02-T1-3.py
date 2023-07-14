# 617 JungEun : 230608 THU mission 22 (1) 
# 2th type1-3
# basic1.csv -> 'age' 컬럼의 이상치(IQR로 구하는 방법)를 더하라.

# 1. Data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Get the std and limit line values of normal data
avg, std = df['age'].mean(), df['age'].std()



# 3. Define abnormal data and Print it
print(df[(df['age'] < avg-std*1.5)|(df['age'] > avg + std*1.5)]['age'].sum())

# 473.5



# 풀이
# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

std = df['age'].std() * 1.5
mean = df['age'].mean()

min_out = mean - std
max_out = mean + std
print(min_out, max_out)
# 5.298862216116952 96.62713778388306


# 이상치 age합
df[(df['age']>max_out)|(df['age']<min_out)]['age'].sum()

# 다르게 작성방법
# df.loc[(df['age'] > max)]['age'].sum() + df.loc[(df['age']< min)]['age'].sum()
