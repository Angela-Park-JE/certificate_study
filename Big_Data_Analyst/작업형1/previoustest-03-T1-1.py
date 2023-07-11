# 617 JungEun : 230607 WED mission 21 (1)
# 3th type1-1
# 2022년 데이터 중 2022년 중앙값보다 큰 값의 데이터 수

# 1. Data and libraries

import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data2.csv", index_col='year')


# 2. get the year of index '2022' and median
year22 = df.loc[df.index[0], :]
med22 = year22.median()


# 3. count them if over the median
print(len(year22[year22>med22]))

# 50



# solution
m = df.loc["2022년"].median()
print(sum(df.loc["2022년",:] > m))
