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


# 2. 정규성 검정
before, after = df['bp_pre'], df['bp_post']
print(stats.kstest(after - before, 'norm'))  # 전-후

# KstestResult(statistic=0.5486501019683699, pvalue=1.9590241771265486e-34)
# 정규성 테스트 H0: 정규분포와 차이 없음 H1: 차이 있음
# 0.05보다 작으면 귀무가설 기각, pvalue0.05 보다 작으므로 정규성과 유의미한 차이 있음

# 지수표현 풀기
# np.set_printoptions(suppress=True)
# pd.options.display.float_format = '{:.6f}'.format   # 6째 자리까지 표현
# pd.reset_option('display.float_format')


# 3. 
