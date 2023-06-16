# 617 JungEun : 230609 FRI mission 23 (2) 
# T1-24 lagged time data 만들기
# basic2 데이터에서 "pv"컬럼으로 1일 시차(lag)가 있는 새로운 컬럼을 만들고 (데이터를 하루씩 미루고)
# 새로운 컬럼의 1월 1일 데이터는 1월 2일 데이터로 채운 다음
# Events가 1이고 Sales가 1000000 이하인 새로운 'pv'컬럼의 합 구하라
# https://www.kaggle.com/code/angellapark/t1-24-time-series5-lagged-feature/


# 1. Data and libraries
import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
# df.info()



# 2. Do lagging
# 'PV'를 마지막 데이터 하나를 빼고 리스트화해서
pvlist = list(df.loc[:, 'PV'][:-1])



# 3. Fill the 01-01 value with 01-02 value
# 해당 리스트에서 1번째인 2일차를 1일차에 넣도록 리스트를 더합니다
pvlist = [pvlist[0]] + pvlist
# 리스트를 새 컬럼을 만들어 넣습니다
df['PV_lagged'] = pvlist



# 4. Condition : 'Events' == 1 AND 'Sales' <= 1000000
answer = df[(df['Events'] == 1)&(df['Sales'] <= 1000000)]['PV_lagged'].sum()
print(answer)
# 1894876


# ---
# 풀이

import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
df

# 결측치 확인
df.isnull().sum()

#1일 차이가 나는 시차 특성 만들기
df['previous_PV'] = df['PV'].shift(1)
df.head()

# 1일 씩 미뤘음으로 가장 앞이 결측값이 됨 (바로 뒤의 값으로 채움)
df['previous_PV'] = df['previous_PV'].fillna(method = 'bfill')
df.head()

# 조건에 맞는 1일 이전 PV의 합
cond = (df['Events'] == 1) & (df['Sales'] <= 1000000)
print(df[cond]['previous_PV'].sum())

# 답 : 1894876.0
