# 617 JungEun : 230524 WED - Mission 9 (1)
# T1-5. 조건에 맞는 데이터 표준편차 구하기
# 주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오


# 1. Load data and libraries
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. 'ENFJ', 'INFP' data and thier standard deviations
std_enfj, std_infp = df[df['f4'] == 'ENFJ']['f1'].std(), df[df['f4'] == 'INFP']['f1'].std()



# 3. Print the diff to an absolute value
print(abs(std_enfj - std_infp))
