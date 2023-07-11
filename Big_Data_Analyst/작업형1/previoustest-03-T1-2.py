# 617 JungEun : 230607 WED mission 21 (1)
# 3th type1-2
# 결측치 데이터(행)을 제거하고, 앞에서부터 60% 데이터만 활용해, 'f1' 컬럼 3사분위 값을 구하시오

# 1. Data and libraries
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")


# 2. Drop the missing values' row
df2 = df.dropna(axis = 0)
cutline = int(df2.shape[0]*0.6)
df2 = df2[:cutline]


# 3. get Q3
import numpy as np
print(np.percentile(df2['f1'], 75))

# 77.25



# solution
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")
df = df.dropna()
df = df.iloc[:int(len(df)*0.6)]
print(df['f1'].quantile(.75))
