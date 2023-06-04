# 617 JungEun : 230527 SAT mission 12 (1)
# T1-12. 그룹화, 상위10, 하위10개
# 접종률 상위 10개 국가의 평균과 접종률 하위 10개 국가의 평균 차이 구하기, 
# 100 퍼센트가 넘는 접종률은 제거, 소수 첫째 자리까지.

# 1. Load Data and Libraries 
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv')



# 2. vaccinated ratio max value of each country
# 'ratio' column = 'people_vaccinated' / 'population' * 100
sr_vrate = df.groupby('country')['ratio'].max()
# and ordering by values
sr_vrate.sort_values(inplace = True, ascending = False)
# delete the values which are over 100
sr_vrate = sr_vrate[~(sr_vrate>100)]



# 3. top 10 and end 10
head10, tail10  = np.mean(sr_vrate.head(10)), np.mean(sr_vrate.tail(10))



# 4. print the diff
print(format(head10 - tail10, '.1f'))
