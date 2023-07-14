# 617 JungEun : 230608 THU mission 22 (1) 
# 2th type1-2
# 데이터셋의 70% 데이터만 활용하여 'f1' 컬럼 결측치를 중앙값으로 채우기 전, 후의 표준편차를 구하여 두 값의 차이 계산하기

# 1. Data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Set the data with 70% rows
length = int(len(df)*0.7)
df = df[:length]



# 3. Get 'f1' median and fill the missing values, and Get the standard deviations
df2 = df['f1'].fillna(df['f1'].median())
std1, std2 = df['f1'].std(), df2.std()



# 4. Diff
print(std1-std2)

# 3.2965018033960725



# 풀이
# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# 데이터 나누기 방법1
data70 = df.iloc[:70]
data30 = df.iloc[70:]

# 데이터 나누기 방법2 : np.split 함수 이용, 길이의 0.7만큼까지 데이터 나누기.
# data70, data30 = np.split(df, [int(.7*len(df))])

# (랜덤 샘플링이 지시되었을 경우) 데이터 나누기 방법3 : 랜덤 샘플링하라고 했을 때, sample로 0.7만큼 뽑고 index 리셋시키기.
# data70 = df.sample(frac = 0.7)
# data70 = df.drop(data70.index)

data70.tail()

## 결측치 확인
data70.isnull().sum()

## 결측치 채우기 전 f1컬럼 표준편자
std1 = data70['f1'].std()
std1

## 중앙값 확인
med = data70['f1'].median()
med

## 중앙값으로 채우기
data70['f1'] = data70['f1'].fillna(med)

## 다른 방법들
# data70['f1']= data70['f1'].replace(np.nan, med)
# data70 = data70.fillna(value=med)

## 결측치 확인
data70.isnull().sum()

## 결측치를 채운 후 표준편차 구하기
std2 = data70['f1'].std()
std2

print(std1-std2)
