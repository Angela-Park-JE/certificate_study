# 617 JungEun : 230602 FRI mission 17 (2)
# T1-21. 이상치 제거, 구간 분할
# 'age'컬럼의 이상치를 제거하고 동일한 개수로 나이 순 3그룹 만들어, 각 그룹의 중앙값을 더하라

# 1. Data and libraries
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Drop the abnormal data in 'age' : set the condition and define a new data
# If I have to use IQR : this case doesn't have missing values following this condition
q1, q3 = df['age'].quantile(0.25), df['age'].quantile(0.75)
IQR = q3 - q1
cond1 = (df['age']>(q1 - IQR*1.5))&(df['age']<(q3 + IQR*1.5))
# And the minus intager, zero, and float numbers
cond2 = (df['age']>0)&(df['age']%1==0)

df = df[cond1&cond2]



# 3. Binning to 3 groups with the same length in 'age' column ordering, sum the medians of them.
# 순서를 정리 후
df.sort_values(by = 'age', inplace = True)
# 길이를 정하여 그대로 3개로 나눕니다.
l = int(round(len(df))/3)

m1 = df[:l*1]['age'].median()
m2 = df[l*1:l*2]['age'].median()
m3 = df[l*2:]['age'].median()



# 4. Print the sum of median values
print(m1+m2+m3)
