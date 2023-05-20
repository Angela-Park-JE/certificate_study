## 주어진 데이터는 고혈압 환자 치료 전후의 혈압이다. 해당 치료가 효과가 있는지 대응(쌍체)표본 t-검정을 진행하시오. 다음을 출력한다.
# - 귀무가설(H0): 𝜇 >= 0
# - 대립가설(H1): 𝜇 < 0
# - 𝜇 = (치료 후 혈압 - 치료 전 혈압)의 평균
# - 유의수준: 0.05


# library import
import pandas as pd
import numpy as np
from scipy.stats import *

# data load
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/high_blood_pressure.csv")

# your code

# check the lengths of 'pre' and 'post' 
# df.info()



# 1. average of (post - pre) blood pressure : round off 2
# mean_bp_diff = round(np.mean(df['bp_post'] - df['bp_pre']), 2)
# print(mean_bp_diff)

bp_diff = df['bp_post'] - df['bp_pre']
print(round(np.mean(df['bp_post'] - df['bp_pre']), 2))



# 2. test and statistic(the statistic, round off 4)
    # (1) normality test : 
    # [H0: 정규분포와 차이가 없다| H1: 정규분포와 차이가 있다.]
before, after = df['bp_pre'], df['bp_post']
#stats.kstest(after - before, 'norm')
    # the p-value is less than 0.05, so we can't consider that this diff doesn't satisfy normality. 
    # (2) paired sample t-test : (before, after) If the therapy, 'after' will be less than 'before'.
    # stats : round off 4 
ttest_stats, ttest_pv = stats.ttest_rel(before, after, alternative = 'greater')
    # same as : `stats.ttest_rel(after, before, alternative = 'less')`
print(round(ttest_stats, 4))



# 3. p-value(round off 4)
print(round(ttest_pv, 4))



# 4. Can we say it worked? (alpha = 0.05)
# p-value(0.0016) < 0.05 (one-sided test)
print('귀무가설 기각')



# result
# -6.12
# 3.0002
# 0.0016
# 귀무가설 기각
