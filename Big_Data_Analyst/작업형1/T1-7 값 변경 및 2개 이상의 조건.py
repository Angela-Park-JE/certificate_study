# 617 JungEun : 230525 THU - Mission 10 (1)
# T1-7. 값 변경 및 2개 이상의 조건
# 'f4'컬럼의 값이 'ESFJ'인 데이터를 'ISFJ'로 대체하고, 'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력하시오!

# 1. Load data and libraries
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Replace 'f4' column's data : 'ESFJ' -> 'ISFJ' 
df['f4'].replace('ESFJ', 'ISFJ', inplace = True)



# 3. Set the conditions and get the maximum value.
print(df[(df['city'] == '경기')&(df['f4'] == 'ISFJ')]['age'].max())
