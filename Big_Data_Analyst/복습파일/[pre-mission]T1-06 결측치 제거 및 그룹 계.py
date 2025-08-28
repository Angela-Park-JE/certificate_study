# 250828: 특정 컬럼의 결측치 제거 한 뒤, 
# 'city'와 'f2'를 기준으로 묶어 합계를 구하고,
# 'city'가 경기이면서 f2가 0인 조건에 만족하는 f1값을 구하라

import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
# df.head(3)

# 먼저 결측치 제거
df.dropna(axis = 0, subset = ['f1'], inplace = True)

# 그룹 합계 계산
df_pt = df.pivot_table(values = 'f1', index = 'city', columns = 'f2', 
                       aggfunc = 'sum')
# df_pt  # 행이 city 열이 f2로 이루어진 피벗테이블 형테

# 조건에 맞는 값을 구하기
print(df_pt.loc['경기', 0])
