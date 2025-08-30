# 250830:
# library import
import pandas as pd
import numpy as np
from scipy.stats import *
# data load
df = pd.read_csv('/kaggle/input/bigdatacertificationkr/high_blood_pressure.csv')

# check the lengths of 'pre' and 'post'
# df.info()


### 1. 처치 전과 처치 후의 혈압 차이에 대해 평균을 구하여 소수점 2자리
df['bp_gap'] = df['bp_post'] - df['bp_pre']
# df
answer = round(np.mean(df['bp_gap']), 2)
print(answer)


