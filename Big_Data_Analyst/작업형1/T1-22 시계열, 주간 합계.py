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

# 90899560 # 답은 맞았음



# --- 
# 배운점
# - 내 방법의 경우 week 즉 년의 몇 번째 주인지에 따라 그룹을 해버린다. 
#   있는 주 즉 해당 년이 월요일부터 시작하지 않을 경우 월요일 이전의 데이터는 버리고 계산한다. 주의 시작을 월요일로 본다. 
#   (아마 비즈니스 데이를 따라서 일요일 시작이 아니라 월요일 시작을 default값으로 가진것 같다. 뒤에 적어두었지만 버려진 날들을 해당 년 마지막 주에 포함시켜버린다. 🤯)
# - 그러나 풀이에서 제공하는 방법은 주 단위로 잘라서 그룹을 한다. 
#   데이터가 월요일부터 시작하지 않을 경우, 이전의 데이터를 버리지 않고 취합하여 하나의 주라고 취급한다. 말그대로 "X요일 ~ 일요일" 까지 합하는 식이다.

# ---
# 풀이
# 라이브러리 및 데이터 로드
import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv", parse_dates=['Date'], index_col=0)

# 아래 코드를 한줄로 표현함
# df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.set_index('Date')

# print(df.shape)
# df.head(3)

# 단위
# 주 단위 W
# 2주 단위 2W
# 월 단위 M
df_w = df.resample('W').sum()
# df_w.head()
# df_w.shape


ma = df_w['Sales'].max()
ma
mi = df_w['Sales'].min()
mi

print(ma - mi)
