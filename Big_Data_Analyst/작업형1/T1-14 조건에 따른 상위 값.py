# 617 JungEun : 230530 TUE mission 14 (1)
# T1-14. 조건에 따른 상위 값
# 'city'와 'f4' 기준 'f5'의 평균값을 구하고 해당 값에서 'f5' 기준으로 상위 7값을 모두 더해 출력


# 1. Load Data and Libraries 
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Aggregating by 'city' and 'f4' to get grouped average values
df_agg = pd.pivot_table(data = df, index = ['city', 'f4'], values = 'f5' , aggfunc = 'mean')
# and order by 'f5', descending
df_agg.sort_values(by = 'f5', ascending = False, inplace = True)



# 3. Get the sum of them, top 7
# method 1 : 인덱스를 아예 풀어버리기 ('city'만 드랍하는 방법도 있을 수 있겠죠)
df1 = df_agg.reset_index()
sum1 = sum(df1.iloc[:7, 2])   # 'f5'는 세 번째에 위치 : 643.6813362975
# method 2 : 멀티인덱스 접근하기
df2 = df_agg[:][:7][:]
sum2 = sum(df2['f5'])    # : 643.6813362975
# method 3 : 인덱스 계층 타고 값에 접근하기 ('city-f4' 기준으로 으로 각각 다른 값을 갖기 때문에 여기서는 두 번째와 같은 방식)
df3 = df_agg[:][:][:7]
sum3 = sum(df3['f5'])    # : 643.6813362975

print(format(sum1, '.2f'))
