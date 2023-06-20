# 617 JungEun : 230610 SAT mission 24 (3)
# T1-28 13시 이전 데이터를 추려서, 오더가 많았던 날짜를 형식 그대로 가져온다

# 1. Data and libraries
import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/payment.csv")



# 2. Cut by 'hour' anc count
ordercnt = df[df['hour']<13].value_counts('date')



# 3. Print!
print(ordercnt.index[0])



#---
# 풀이
print(df[df['hour'] < 13]['date'].value_counts().index[0])

# 답 : 20221203
