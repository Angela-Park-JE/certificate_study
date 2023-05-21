### **미션3. 수: 작업형3 단일표본 가설검정**
# [파이썬 링크]([https://www.kaggle.com/agileteam/t3-ttest-1samp](https://www.kaggle.com/agileteam/t3-ttest-1samp))

## 문제
# 다음은 22명의 학생들이 국어시험에서 받은 점수이다. 학생들의 평균이 75보다 크다고 할 수 있는가?
# - 귀무가설(H0): 모평균은 mu와 같다. (μ = mu), 학생들의 평균은 75이다
# - 대립가설(H1): 모평균은 mu보다 크다. (μ > mu), 학생들의 평균은 75보다 크다
# 가정:
# - 모집단은 정규분포를 따른다.
# - 표본의 크기가 충분히 크다.
# ### 지시된 작업
# **검정통계량, p-value, 검정결과를 출력하시오**



# 617 JungEun : 230517 - warming up mission

# data and library

import pandas as pd
from scipy.stats import *

scores = [75, 80, 68, 72, 77, 82, 81, 79, 70, 74, 76, 78, 81, 73, 81, 78, 75, 72, 74, 79, 78, 79]
series = pd.Series(scores)

m = 75
a = 0.05

# skip: normality satisfied (Hypothesis)

# one sample t-test

stats, pval = ttest_1samp(series, 75, axis=0, nan_policy='propagate', alternative='greater')

# for neatness, round off 4

print(round(stats, 4))
print(round(pval, 4))

if pval < 0.05:
    print('귀무가설 기각. 모평균은 75보다 크다고 말할 수 있다.')
else:
    print('귀무가설 채택. 모평균은 75보다 크다고 말할 수 없다.')



## 결과
# 1.7659
# 0.046
# 귀무가설 기각. 모평균은 75보다 크다고 말할 수 있다.
