# 어떤 특정 약물을 복용한 사람들의 평균 체온이 복용하지 않은 사람들의 평균 체온과 유의미하게 다른지 검정해보려고 합니다.
# **가정:**
# - 약물을 복용한 그룹과 복용하지 않은 그룹의 체온 데이터가 각각 주어져 있다고 가정합니다.
# - 각 그룹의 체온은 정규분포를 따른다고 가정합니다.

### 지시된 작업
# 1. 검정통계량, p-value, 검정결과를 출력하시오

### 풀이순서
# 1. 데이터 프레임으로 데이터 불러오고 라이브러리 넣기
# 2. `scipy.stats.bartlett()` : 등분산성을 만족하는지 확인(옵션을 위해)
# 3. `scipy.stats.ttest_ind()` : 독립표본 t검정
# 4. 검정통계량, p값, 그리고 유의수준에 따라 메시지를 출력하도록 `print()` 적음



import pandas as pd
from scipy.stats import *

# 데이터 수집
# - 그룹1이 복용한 그룹이고 그룹2가 복용하지 않은 그룹이라고 가정합니다.
# - 같은 샘플에 터리 전후를 비교하지 않기 때문에 쌍체 t검정이 아닌 독립표본 t검정을 합니다. 
group1 = [36.8, 36.7, 37.1, 36.9, 37.2, 36.8, 36.9, 37.1, 36.7, 37.1]
group2 = [36.5, 36.6, 36.3, 36.6, 36.9, 36.7, 36.7, 36.8, 36.5, 36.7]



# (1) data:
# (꼭 만들 필요는 없으나 문제에서 데이터가 각각의 csv 파일 등으로 존재할 경우 불러왔을때 판다스로 작업하는 경우가 많을 것이라는 예상 하에 만들었습니다.)
d = {'g1':group1, 'g2':group2}
df = pd.DataFrame(data = d)
# df.info()



# (2) equal-variance test
# Bartlett test: H0 = equal-var (O) | H1 equal-var (X)
# bartlett(df['g1'], df['g2'])
# pvalue=0.8351, so the samples can be considered for satisfying equal variance
# (결과 따라 자동으로 옵션을 넣도록 해도 되지만, 실제 시험장에서도 눈으로 값을 확인하는 과정을 가질것 같아 두었습니다.)



# (3) Independent samples t-test
# (alpha는 0.05로 가정합니다.)
stats, pval = ttest_ind(df['g1'], df['g2'], equal_var = True, alternative = 'two-sided')
print(stats)
print(pval)
if pval < 0.05:
    print('귀무가설 기각. 유의미한 차이가 있다고 볼 수 있다.')
else:
    print('귀무가설 채택. 유의미한 차이가 있다고 볼 수 없다.')



# result
# 3.7964208654863336
# 0.001321891476703691
# 귀무가설 기각. 유의미한 차이가 있다고 볼 수 있다.
