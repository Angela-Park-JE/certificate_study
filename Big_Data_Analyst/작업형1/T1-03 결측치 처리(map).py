# 617 JungEun : 230523 TUE - Mission 8 (1)
# T1-3. 결측치 처리
# 주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고,
# 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력하세요!



# 1. Load data and libraries
import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Check the empty values ratio in each columns 
# and drop the columns which have null values(>80%)
# 전에는 일일히 출력하면서 확인하고 했는데, 최대한 결과 출력을 덜 해보는 방향으로 적어보려고 했어요.

# 기존 확인 방법
# print(df.isna().sum() / len(df))

# 시리즈 형태로 반환되는 것을 이용하여 
s_nullratio = df.isna().sum() / len(df)
# 80 퍼센트 이상 되는 컬럼들을
col_80list = list(s_nullratio[s_nullratio.values >= 0.8].index)
# 바로 넣어서 지워버립니다.
df.drop(columns = col_80list, inplace = True)



# 3. Get the aggregated values with 'city' column about some columns(<80%)
# 80 미만인 컬럼들을 가지고
col_nalist = list(s_nullratio[(s_nullratio.values < 0.8)&(s_nullratio.values > 0)].index)
# 'city'별 중앙값을 그룹바이로 출력하여 데이터프레임으로 만들었어요. 물론 f1 컬럼 하나인건 알지만... 
df_median = df.groupby('city')[col_nalist].median()
# 여러 개면 이렇게도 돌려줄 수 있겠죠. 결측치있는의 도시별 median이 {도시: value} 형태로 들어갑니다.
dict_list = []     # list comprehension은 쓰지 않았어요 한 줄이 너무 길어지니까요 ㅇ_<
for i in col_nalist:
    s = df_median.loc[:, i]
    d = dict(zip(list(s.index), list(s.values))) # <---- 요기!
    dict_list.append(d)



# 4. Replace using dict_list
# 결측치 있는 컬럼과 해당 컬럼 집계값 딕셔너리가 같은 순서로 넣어져있을테니 zip을 써서 동시에 불러왔어요.
for j, k in zip(col_nalist, dict_list):
    df[j] = df[j].fillna(df['city'].map(k))



# 5. FINALLY... Print the average of 'f1' column
print(df['f1'].mean())
