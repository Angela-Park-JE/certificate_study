# 617 JungEun : 230522 MON - Mission 7 (1)
# T1-1. 이상치를 찾아라
# 데이터에서 IQR을 활용해 Fare컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오

# 1. Load Data and Library 
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/c/titanic/train.csv')
# df.head(3)



# 2. SET IQR 
Q1 = np.percentile(df['Fare'], 25)
Q3 = np.percentile(df['Fare'], 75)
IQR = Q3 - Q1



# 3. Find the outliers
df_outs = df[(df['Fare'] < Q1 - IQR*1.5)|(df['Fare'] > Q3 + IQR*1.5)]



# 4. Get the number of female passengers.
print(len(df_outs[df_outs['Sex'] == 'female']))



# AND simply like this(step 3 + step 4)
# 공부한다고 몇주 전 했었을때 이렇게 했었어요. 이상치 데이터에 조건 걸고 sum을 때리는 겁니다!
# print(sum(df[(df['Fare']< q1-(q3-q1)*1.5)|(df['Fare']> q3+(q3-q1)*1.5)]['Sex']=='female'))
