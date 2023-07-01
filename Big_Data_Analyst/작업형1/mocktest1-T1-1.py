# 617 JungEun : 230612 MON mission 25 (1)
# 모의고사 T1-1
# 데이터를 50:50으로 나누어서 앞은 A 뒤는 B.
# A는 'f1' 결측치를 A그룹에서의 중앙값으로, B는 'f1'의 결측치를 B그룹에서의 최대값으로 채운 뒤, A그룹과 B그룹의 표준편차 합을 구하라
# 결과는 둘째자리에서 반올림하여 첫쨰자리까지 출력

# 1. Data and libraries
import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")



# 2. divide the group
l = int(len(df)/2)
df_a, df_b = df.iloc[:l, :], df.iloc[l:, :]



# 3. `fillna` with median and maximum values.
df_a.loc[:, 'f1'] = df_a['f1'].fillna(df_a['f1'].median())
df_b.loc[:, 'f1'] = df_b['f1'].fillna(df_b['f1'].max())


# 4.  standard deviation of each values and Sum them 
print(round(df_a.loc[:,'f1'].std() + df_b.loc[:, 'f1'].std(), 1))
