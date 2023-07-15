# 617 JungEun : 230612 MON mission 25 (1)
# 모의고사 T2-1
# 데이터 셋의 짝수번째 인덱스만 선택하여 꽃잎 너비 컬럼 다 더하기


# 라이브러리 불러오기
import pandas as pd

# data생성 코드(변경금지)
from sklearn.datasets import load_iris
dataset = load_iris()
data_df = pd.DataFrame(dataset.data, columns=dataset.feature_names )
data_df.to_csv("data.csv", index=False)
del data_df, dataset

# 초기 제공 코드
df = pd.read_csv("data.csv")

# your code

print(sum(df[::2]['petal width (cm)']))

# 91.4



# ---
# 풀이
# your code
print(sum(df.iloc[::2,:]['petal width (cm)']))
