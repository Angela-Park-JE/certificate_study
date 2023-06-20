# 617 JungEun : 230610 SAT mission 24 (4)
# T1-29 : 시계열 포맷
# payment 데이터에서 12월인 데이터 수

# 1.Data and libraries
import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/payment.csv")



# 2. transform the date column in a format
# 문제에서 힌트가 있어서 하긴 했는데 아니었으면 date 포맷 말고 string 슬라이싱으로 풀었을 것 같다.
# 포맷지정 안하면 특정일-시간을 나타내는 숫자로 바뀜. 날짜포맷은 SQL 생각하고 했더니 잘 되었음.
df['date'] = pd.to_datetime(df['date'], format = '%Y%m%d')



# 3. by month
print(len(df[df['date'].dt.month == 12]))



# ---
# 풀이

df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
print(sum(df['date'].dt.month == 12))

# 답 : 11
