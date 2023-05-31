# 617 JungEun : 230526 FRI - Mission 11 (1)
# T1-9. 표준화(standardization - NOT normalization)
# basic.csv의 'f5' 컬럼을 표준화 하고 그 중앙값을 구하라

# 1. Load data and libraries
import pandas as pd
import numpy as np
import sklearn.preprocessing

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Standardization : scikitlearn - preprocessing 
scaler = sklearn.preprocessing.StandardScaler()
scaled_f5 = scaler.fit_transform(df[['f5']]) # nd.array 형태



# 3. Get median : median = Q2
# print(np.percentile(scaled_f5, 50))
# print(np.quantile(scaled_f5, 0.5))
print(np.median(scaled_f5))
