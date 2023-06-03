# 617 JungEun : 230525 THU - Mission 10 (2)
# T1-8. 누적합 그리고 보간, 결측치 처리
# 주어진 데이터 셋에서 'f2' 컬럼이 1인 조건에 해당하는 데이터의 'f1'컬럼 누적합을 계산한다. 
# 누적합은 백워드필을 이용, (단, 결측치 바로 뒤의 값이 없으면 다음에 나오는 값을 채워넣는다) 최종적으로 누적합의 평균값을 출력한다. 

# 1. Load data and libraries
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Set a new dataset, following the condition: 'f2' = 1
df_temp = df[df['f2'] == 1]



# 3. New column for calculating the cumulative sums
df_temp['f1_cumsumed'] = np.cumsum(df_temp['f1'])
# 산술은 결측치를 제외하고 하게 되기 때문에 결측치가 있는 부분은 cumsum도 똑같이 결측일 것입니다.



# 4. fillna with back data - backward fill method
df_temp['f1_cumsumed'].fillna(method = 'bfill', inplace = True)
# 잘 들어갔는지 확인하고자 한다면 이것을 실행해서 f1이 NaN인 데이터에 f1_cumsum이 잘 들어갔는지 보면 됩니다.
# df_temp[df_temp['f1'].isna()]



# 5. Print the cumulative sum's average
print(df_temp['f1_cumsumed'].mean())
