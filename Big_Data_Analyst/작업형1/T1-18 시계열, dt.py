# 617 JungEun : 230601 THU mission 16 (1)
# T1-18. 시계열 데이터
# 2022 5월의 주말과 평일의 'Sales' 평균 차이 구하라. 반올림으로 소수점 둘째 자리 까지.


# 1. Load Data and Libraries 
import pandas as pd
import datetime

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic2.csv')



# 2. Set a date and 2022 may data
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Date'].dt.strftime('%Y%m')=='202205']



# 3. 2022 May's weekdays
workdays = pd.date_range('2022-05-01', '2022-5-31', freq='B')
workdays = list(workdays)



# 4. Average values of weekdays and weekend
b_avg = df[df['Date'].isin(workdays)]['Sales'].mean()
w_avg = df[(~df['Date'].isin(workdays))]['Sales'].mean()



# 5. Print the diff
print(round(abs(b_avg - w_avg), 2))
