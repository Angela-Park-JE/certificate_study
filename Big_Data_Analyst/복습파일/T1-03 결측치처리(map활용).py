import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
df.head(3)

# EDA - 결측값 확인(비율 확인)
df.info()

# 80%이상 결측치 컬럼, 삭제
df.isna().sum()/len(df)
df.drop(columns = 'f3', inplace = True)
df.head(3)

# city 별 중앙값 및 대체
df_med = df.groupby('city').median()
print(df_med)

fill_median_func = lambda m: m.fillna(m.median()) # numeric only 관련 옵션이 필요하게 된다고 경고가 같이 
df_filled = df.groupby('city').apply(fill_median_func)
df_filled.head(3)

# f1 평균값 내어 결과 출력
print(df_filled['f1'].mean())
