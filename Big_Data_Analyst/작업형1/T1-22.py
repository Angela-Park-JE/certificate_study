# T1-22. Time-Series4 (Weekly data)

# 617 JungEun : 230603 SAT mission 18 (1)
# T1-22. 시계열 데이터, 주간 합계
# 주어진 데이터셋에서 주간 합계가 가장 큰 주와 가장 작은 주의 차이를 절댓값으로 나타내라

# 1. Data and libraries
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic2.csv', parse_dates=['Date'])



# 2. Aggregate by week, dividing 2022 and 2023 year information.
# 그룹화 전 22, 23 년으로 있으니 먼저 년을 나눕니다.
df22, df23 = df[df['Date'].dt.year == 2022], df[df['Date'].dt.year == 2023]
# dt.week는 사라졌으니 `Series.dt.isocalendar().week`을 쓰라는 워닝을 받고 했는데 값이 같아서 그대로 가져왔습니다.
# 연을 나눈 것을 주 단위로 groupby 시킵니다.
df_22weekly = df22.groupby(by = df22['Date'].dt.isocalendar().week).sum()
df_23weekly = df23.groupby(by = df23['Date'].dt.isocalendar().week).sum()
# 연단위로 나눈 데이터를 비교하기 위해 하나로 합칩니다.
df_allweekly = pd.concat([df_22weekly, df_23weekly], axis = 0, ignore_index = True)



# 3. Get the weekly max 'Sales' value and minimum value.
maxsales = df_allweekly['Sales'].max()
minsales = df_allweekly['Sales'].min()
print(abs(maxsales - minsales))
