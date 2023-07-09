# T1-2. (loves반응+wows반응)/(reactions반응) 비율이 0.4보다 크고 0.5보다 작으면서, type 컬럼이 'video'인 데이터의 갯수

# 617 JungEun : 230606 TUE mission 20 (1)
# 4th type1-2

import pandas as pd
df = pd.read_csv("/kaggle/input/big-data-analytics-certification-kr-2022/fb.csv")

df['good_reacts'] = (df['loves']+df['wows'])/df['reactions']
print(len(df[(df['good_reacts'] >0.4)&(df['good_reacts'] <0.5)&(df['type'] == 'video')]))

# 90



# 풀이
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/fb.csv")
cond1 = (df['loves'] + df['wows'])/ df['reactions'] > 0.4
cond2 = (df['loves'] + df['wows'])/ df['reactions'] < 0.5
cond3 = df['type'] == 'video'

print(len(df[cond1 & cond2 & cond3]))
