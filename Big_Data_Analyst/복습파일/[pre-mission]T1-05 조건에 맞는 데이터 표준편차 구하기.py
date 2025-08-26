# 250826: 조건에 맞는 데이터를 한정하여 표준편차를 구한 후
# 두 표준편차의 절댓값을 구하기!
import numpy as np
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
# df.head(3)

df_enfj = df[df['f4'] == 'ENFJ'][['f4', 'f1']]
df_infp = df[df['f4'] == 'INFP'][['f4', 'f1']]

std_enfj, std_infp = df_enfj['f1'].std(), df_infp['f1'].std()
print(np.abs(std_enfj - std_infp))
