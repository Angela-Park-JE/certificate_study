# 617 JungEun : 230522 MON - Mission 7 (2)
# T1-2. 이상치를 찾아라
# 주어진 데이터에서 이상치(소수점 나이)를 찾고 올림, 내림, 버림(절사)했을때 3가지 모두 이상치 'age' 평균을 구한 다음 모두 더하여 출력하시오.


# 1.Load Data and Libraries
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
# df.head(3)



# 2. Get the data(float values)
df_outs = df[df['age']%1 != 0]



# 3. np.ceil, floor, trunc
avg_ceil = np.ceil(df_outs['age']).mean()
avg_floor = np.floor(df_outs['age']).mean()
avg_trunc = np.trunc(df_outs['age']).mean()



# 4. Sum them
print(avg_ceil+avg_floor+avg_trunc)
