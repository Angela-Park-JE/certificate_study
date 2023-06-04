# 617 JungEun : 230527 SAT mission 12 (2) - 상관관계가 큰 피처와 작은 피처의 값을 더하여 출력 - 정답
# T1-13. 상관관계
# quality 와 상관관계가 가장 큰 값과 가장 작은 값을 구하여 더하여 소수점 둘째 자리까지 출력.
# 주의할 것: 상관관계가 크다라는 의미는 상관계수 절대값이 크다는 말로 이해하자.

# 1. Load Data and Libraries 
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/red-wine-quality-cortez-et-al-2009/winequality-red.csv')



# 2. Get correlation matrix 
df_corr = df.corr()
# and absolute value for the correlation strength : 아예 해당 컬럼만, 시리즈로, 절댓값으로 변환하여 넣습니다.
sr_qual = abs(df_corr['quality'])
# and delete the correlation with itself ('quality') : 자기 자신 상관계수만 지웁니다
sr_qual = sr_qual[sr_qual.values != 1]
# and get max and min : 그리고 최대 최소 상관계수 절대값을 구합니다. 
max_val = sr_qual.max()
min_val = sr_qual.min()



# 3. sum them and print it 
print(format(max_val + min_val, '.2f'))
