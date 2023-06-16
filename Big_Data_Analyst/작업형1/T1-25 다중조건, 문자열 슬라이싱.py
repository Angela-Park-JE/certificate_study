# 617 JungEun : 230609 FRI mission 23 (3) 
# T1-25 STR slicing
# basic1 데이터에서 f4가 E로 시작하면서 부산에 살고 20대인 사람 명 수


# 1. Data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2.'f4' == E@@@ AND 'city' == 부산 AND 'age' == 20s
cond1 = df['f4'].str[:1] == 'E'
cond2 = df['city'] == '부산'
cond3 = (df['age']>=20)&(df['age']<30)



# 3. Count them
print(len(df[cond1&cond2&cond3]))
# 0



# ---
# 풀이
import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df['EI'] = df['f4'].str[:1]
cond1 = df['EI'] == "E"
cond2 = df['city'] == "부산"
cond3 = (df['age'] >= 20) & (df['age'] < 30)

print(len(df[cond1 & cond2 & cond3]))


# 답 : 0
