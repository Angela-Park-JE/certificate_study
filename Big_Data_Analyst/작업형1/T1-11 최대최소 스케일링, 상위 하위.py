# 617 JungEun : 230526 FRI - Mission 11 (2)
# T1-11. min-max scaling, top 5% low 5% 
# 주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오

# 1. Load data and libraries
import pandas as pd
import numpy as np
import sklearn.preprocessing

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. min-max scaling
# help(sklearn.preprocessing.minmax_scale)
df['f5_MMscaled'] = sklearn.preprocessing.minmax_scale(df['f5'])



# 3. Get the value of top 5% and low 5% and sum
print(np.percentile(df['f5_MMscaled'], 5) + np.percentile(df['f5_MMscaled'], 95))
