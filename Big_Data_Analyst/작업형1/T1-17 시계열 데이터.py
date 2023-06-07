# 617 JungEun : 230530 WED mission 15 (2)
# T1-17. 시계열 데이터, 날짜 다루기
# 2022 5월 'Sales' 중앙값 구하라

# 1. Data and libraries
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic2.csv')



# 2. admit the types : datetime 
df['Date'] = pd.to_datetime(df['Date'])
df2 = df.set_index('Date')



# 3. 2022 may Sales
df2.loc['2022 May', 'Sales'].median()
