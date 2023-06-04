# 617 JungEun : 230530 TUE mission 14 (2)
# T1-15. 슬라이싱과 조건, 결측치 대체
# age 컬럼 상위 20개 데이터에 대해 f1의 결측치를 중앙값으로 채운다.
# 'f4'가 'ISFJ'이고 'f5'가 20이상인 'f1'의 평균값을 출력하라

# 1. Load Data and Libraries 
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. 'age' top 20 data : replace with their median
df_top20 = df.sort_values(by = 'age', ascending = False)[:20]
df_top20['f1'].fillna(df_top20['f1'].median(), inplace = True)



# 3.'f4' = 'ISFJ', 'f5'>= 20 : Print 'f1' average 
cond1 , cond2 = df_top20['f4'] == 'ISFJ' , df_top20['f5'] >= 20
print(df_top20[cond1&cond2]['f1'].mean())
