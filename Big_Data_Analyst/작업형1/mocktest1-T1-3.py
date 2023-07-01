# 617 JungEun : 230612 MON mission 25 (3)
# 모의고사 T1-3
# 'age' 컬럼에서 IQR 방식으로 거른 이상치 개수 + std*1.5를 이용한 이상치 개수
# (표준편차1.5방식: 평균으로부터 '표준편차1.5'를 벗어나는 영역을 이상치라고 판단함)

# 1. Data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
age = df['age']


# 2. IQR method
q1, q3 = age.quantile(0.25), age.quantile(0.75)
IQR = q3 - q1
abnorm_byIQR = len(age[(age < q1 - IQR*1.5)|(age > q3 + IQR*1.5)])


# 3. std method
m, s = age.mean(), age.std()
abnorm_bySTD = len(age[(age < m - s*1.5)|(age > m + s*1.5)])


# 4. Sum the results
print(abnorm_byIQR + abnorm_bySTD)
