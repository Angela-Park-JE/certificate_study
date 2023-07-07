# 공식 예시문제 유형 3 도전
# 617 JungEun : 230605 MON mission 19 (1)
# 유형 3

import pandas as pd
import scipy.stats
df = pd.read_csv('data/blood_pressure.csv', index_col=0)


# 1. data set info
# print(df.info())



# 2. (1) average of after-before
df['mu_d'] = df['bp_after'] - df['bp_before']
print(round(df['mu_d'].mean(), 2))   # -5.09



# 3. (2) statistic value of paird_sample ttest
# print(help(scipy.stats.ttest_rel))
s, pval = scipy.stats.ttest_rel(df['bp_after'], df['bp_before'], axis=0, nan_policy='propagate', alternative='less')
print(round(s, 4))    # -3.3372



# 4. (3) p value of paird_sample ttest
print(round(pval, 4))    # 0.0006



# 5. (4) alpha = 0.05, 채택 or 기각?
alpha = 0.05
if alpha > pval:
    print('기각')  # 귀무가설 기준, 기각 출력.
else:
    print('채택')




# 평균 차이 : -5.09 
# 통계량 : -3.3372
# p값 : 0.0006
# 귀무가설 기각여부 : 기각
