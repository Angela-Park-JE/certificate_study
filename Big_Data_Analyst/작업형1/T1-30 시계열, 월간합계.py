# 617 JungEun : 230614 WED mission 27 (1)
# T1-30. 시계열 데이터, 월단 합계
# 12월 25일의 결제금액(price)가 12월 총 결제금액의 몇 %인지 정수로 나타내라

# 1. Data and libraries
import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/payment.csv", parse_dates = ['date'])



# 2. aggregating by month and date
s_monthly = df.groupby(df['date'].dt.month)['price'].sum()
s_daily = df.groupby(df['date'].dt.date)['price'].sum()



# 3. % ?
# print(s_daily.index)
#   Index([2022-11-29, 2022-11-30, 2022-12-01, 2022-12-02, 2022-12-03, 2022-12-25], dtype='object', name='date')
print(int(s_daily[5]/(s_monthly[12])*100))





# ---
# 풀이
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
cond1 = df['date'].dt.month == 12
cond2 = df['date'].dt.day == 25
result = sum(df[cond1 & cond2]['price']) / sum(df[cond1]['price'])
print(int(result*100))


# 답 : 26
