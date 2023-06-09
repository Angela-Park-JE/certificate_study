# 617 JungEun : 230602 FRI mission 17 (1)
# T1-20. 병합, 결측치 제거, 합 구하기
# 'f4'기준으로 basic1, basic3을 병합하고, 병합된 데이터에서 r2 컬럼에 결측치 있을 시 제거, 
# 그리고 앞에서 부터 20개 데이터를 취하여 'f2' 컬럼의 합을 구하라

# 1. Data and libraries
import pandas as pd

df_1 = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
df_2 = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic3.csv')



# 2. Merging them by 'f4' column
df = pd.merge(left = df_1, right = df_2, how = 'left', on = 'f4')
# 아래와 같습니다
# df = df_1.merge(df_2, on = 'f4', how = 'left')



# 3. Drop the missing values in 'r2', select 20 data, and get the sum of 'f2'.
# 이렇게 구한 다음
df_dropped = df.dropna(axis = 'index', subset = ['r2'])[:20]
# 합을 직접 내도 되고
s = df_dropped['f2'].sum()

# 아래처럼 둘을 합쳐 한번에도 가능합니다.
# s = df.dropna(axis = 'index', subset = ['r2'])[:20]['f2'].sum()

print(s)
