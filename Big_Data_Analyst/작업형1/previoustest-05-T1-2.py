# 617 JungEun : 230620 TUE mission 32 (2)
# T1-2. 정상과 위험의 사람 수 차이의 절대값 -> '정수'로 출력
# bmi(체질량지수): 몸무게(kg) / 키(m)의 제곱  
# 정상체중: BMI 18.5이상 ~ 23미만 / 위험체중: BMI 23 이상 ~ 25미만  

# 1. 데이터, 라이브러리
import numpy as np
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0620 - 미션32/5-2bmi.csv')



# 2. new col : '키'의 제곱
# 값이 왜이렇게 큰가 생각하는데 2분정도 썼음
df['bmi'] = (df['Weight']/(df['Height']/100)**2)



# 3. conditions
cond1 = (df['bmi']>=18.5)&(df['bmi']<23)
cond2 = (df['bmi']>=23)&(df['bmi']<25)



# 4. print the counts
norm, warn = len(df[cond1]), len(df[cond2])
print(int(abs(norm - warn)))



# 144
# 7분



# 복습 230913
# 2 번
# 1. data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0620 - 미션32/5-2bmi.csv')

# 2. bmi 
df['bmi'] = df['Weight']/((df['Height']/100)**2)

# 3. condition : 정상체중: BMI 18.5이상 ~ 23미만 / 위험체중: BMI 23 이상 ~ 25미만
answer = abs(len(df[(df['bmi']>=18.5)&(df['bmi']<23)]) - len(df[(df['bmi']>=23)&(df['bmi']<25)]))

print(answer) # 144
