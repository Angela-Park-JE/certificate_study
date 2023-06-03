# 617 JungEun : 230523 TUE - Mission 8 (2)
# T1-4. skewness, kurtosis and log scaling
# 주어진 데이터 중 train.csv에서 'SalePrice'컬럼의 왜도와 첨도를 구한 값과, 
# 'SalePrice'컬럼을 스케일링(log1p)로 변환한 이후 왜도와 첨도를 구해 모두 더한 다음 소수점 2째자리까지 출력하시오


# 1. Load data and libraries
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/house-prices-advanced-regression-techniques/train.csv')
df_temp = df.head(10)


# 2. skewness, kurtosis values of 'SalePrice' columnn
sk, ku = df['SalePrice'].skew(), df['SalePrice'].kurt()



# 3. log scaling using np.log1p()
sk_logged, ku_logged = np.log1p(df['SalePrice']).skew(), np.log1p(df['SalePrice']).kurt()



# 4. Sum them and print it to two decimal places. 
print(format(sk + ku + sk_logged + ku_logged, '.2f'))
