# 617 JungEun : 230530 WED mission 15 (1)
# T1-16. 분산의 차이
# 'f2'가 0인 데이터에 대해 age를 기준으로 오름차순 정렬 후 앞 20개의 데이터에서,
# 'f1'의 결측치를 최소값으로 채우기 전과 후의 분산의 차이를 구하라 (소수점 둘쨰)


# 1. Load Data and Libraries 
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Set the data : 'f2' = 0, ascending by age, and to 20th
df_temp = df[df['f2'] == 0].sort_values(by = 'age')[:20]



# 3. Get the variance, in case of filling the missing values in 'f1' and in case of not filling it.
before = df_temp['f1'].var()
after = df_temp['f1'].fillna(df_temp['f1'].min()).var()



# 4. diff
print(format(before-after, '.2f'))
