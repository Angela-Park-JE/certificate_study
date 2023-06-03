# 617 JungEun : 230524 WED - Mission 9 (2)
# T1-6. 결측치 제거 및 그룹 합계에서 조건에 맞는 값 찾아 출력
# 주어진 데이터 중 basic1.csv에서 'f1'컬럼 결측 데이터를 제거하고, 
# 'city가 경기, f2가 0'인 조건에 만족하는 f1의 합계 집계값을 구하시오

# 1. Load data and libraries
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Drop the missing data in 'f1' 
df_dropnaf1 = df[~df['f1'].isna()]

# 문제에서 원본 데이터 또 불러올 일이 없으니 dropna 를 쓸 수도 있씁니다.
# df.dropna(subset = 'f1', axis = 0, inplace = True)



# 3. Aggregate by 'city', 'f2'
df_agg = pd.pivot_table(df_dropnaf1, index = 'city', columns ='f2', values = 'f1', aggfunc = 'sum')

# + 만약 groupby를 쓴다면
# df_agg = df_dropnaf1.groupby(['city', 'f2'])['f1'].sum()



# 4. Get the value : 'city' == '경기', 'f2' == 0 
# pivottable, groupby 공통 가능 방법들 : 왜 공통으로 되는지는 공부를 했는데도 모르겠습니다 아무튼 loc 만큼 편한게 없긴 합니다...
# df_agg.loc['경기', 0]
# df_agg.xs('경기').xs(0) 

# groupby 결과(계층형 인덱스)에서만 가능해요
# df_agg['경기'][0]

print(df_agg.loc['경기', 0])
