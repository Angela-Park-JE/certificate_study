# 617 JungEun : 230621 WED mission 33 (1)
# T3. 독립성 검정
# 영어와 수학 시험 결과의 독립성이 있는지 검정

# 1. Data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0621 - 미션33/mission33.csv')

# df.head(3)
# english_scores	math_scores
# 0	우수	보통
# 1	보통	우수
# 2	미흡	보통


# 2. counts value : frequency table
df_cnts = pd.DataFrame([df['english_scores'].value_counts().sort_index(), df['math_scores'].value_counts().sort_index()], 
                     columns = list(df['math_scores'].unique()))



# 3. categories data chi2 test
from scipy.stats import chi2_contingency
stats, pv, dof, exp_freq = chi2_contingency(df_cnts, correction = False)



# 4. print
print('stats :', round(stats, 2))
print('p-val :', round(pv, 4))
print('dof :', dof)


# 결과
# stats : 0.18
# p-val : 0.913
# dof : 2



# --- 
# 풀이 - 699 KYJung P님 것 코드

df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0621 - 미션33/mission33.csv')
print(df.head(5))
print(df.info())

# 교차분석
# 두 번주 간 관계가 독립인지 연관성이 있는지 검정
# 카이제곱 검정 통계량을 이용

# counts를 계산하는 dataframe으로 변경을 우선해야 하는듯,,
# https://jae-eun-ai.tistory.com/51
# print(len(df[df['english_scores'] == '우수']))
xf = [ len(df[df['english_scores'] == '우수']), len(df[df['english_scores'] == '보통']), len(df[df['english_scores'] == '미흡'])]
xm = [ len(df[df['math_scores'] == '우수']), len(df[df['math_scores'] == '보통']), len(df[df['math_scores'] == '미흡'])]
count_values = pd.DataFrame([xf, xm], columns = ['우수', '보통', '미흡'], index = ['english_scores', 'math_scores'])
print(count_values)

from scipy.stats import chi2_contingency
stats, pval, dof, freq = chi2_contingency(count_values)
print(stats)
print(pval)
