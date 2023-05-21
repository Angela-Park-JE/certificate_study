### **미션4. 목: Shapiro-Wilk 검정 (정규성 검정)**
# [파이썬 링크]([https://www.kaggle.com/agileteam/t3-shapiro-wilk](https://www.kaggle.com/agileteam/t3-shapiro-wilk)),

# ### **T3-Shapiro-Wilk 문제 :**
# 12명의 수험생이 빅데이터 분석기사 시험에서 받은 점수이다. Shapiro-Wilk 검정을 사용하여 데이터가 정규 분포를 따르는지 검증하시오.
# - 귀무 가설(H0): 데이터는 정규 분포를 따른다.
# - 대립 가설(H1): 데이터는 정규 분포를 따르지 않는다.
# ### 지시된 작업
# Shapiro-Wilk 검정 통계량, p-value, 검증결과를 출력하시오.



# 617 JungEun : 230518 - warming up mission

# 1. data and library import
import pandas as pd
from scipy.stats import *

data = [75, 83, 81, 92, 68, 77, 78, 80, 85, 95, 79, 89]
df = data
alpha = 0.05

# 2. Shapiro-Wilk Test
# "The Shapiro-Wilk test tests the null hypothesis that the data was drawn from a normal distribution."
stats, pval = shapiro(df)
print("Shapiro-Wilk statistic:", stats)
print("Shapiro-Wilk p-value:", pval)

# 3. print the conclusion
if pval >= alpha:
    print('샤피로윌크검정 p값이 {}로 귀무가설 채택, 정규성을 따른다고 볼 수 있다.'.format(round(pval, 4)))
else:
    print('샤피로윌크검정 p값이 {}로 귀무가설 기각, 정규성을 따른다고 볼 수 없다.'.format(round(pval, 4)))



# # 결과
# Shapiro-Wilk statistic: 0.9768090844154358
# Shapiro-Wilk p-value: 0.9676500558853149
# 샤피로윌크검정 p값이 0.9677로 귀무가설 채택, 정규성을 따른다고 볼 수 있다.
