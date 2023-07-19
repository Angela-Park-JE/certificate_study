# 617 JungEun : 230613 MON mission 26 (4)
# 모의고사2 T2 깍두기
# 대학원 입학 예측

### 데이터 불러오기

# 라이브러리 불러오기
import pandas as pd

# 데이터 불러오기
X_train = pd.read_csv("../input/big-data-analytics-certification/t2-2-X_train.csv")
y_train = pd.read_csv("../input/big-data-analytics-certification/t2-2-y_train.csv")
X_test = pd.read_csv("../input/big-data-analytics-certification/t2-2-X_test.csv")

X_train.shape, y_train.shape, X_test.shape



### 간단한 EDA - dtype, null 체크

# 데이터 확인
display(X_train.head(3))
display(X_test.head(3))
display(y_train.head(3))

# 타입 확인
X_train.info()

# 결측치 확인
print(X_train.isnull().sum())
print(X_test.isnull().sum())

# 기초 통계
X_train.describe()

# 타겟 확인 (시험에선 그래프 안됨)
y_train["Chance of Admit "].hist()

# 상관관계 (시험에선 그래프 안됨) X_train.corr()만 사용
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 8))
sns.heatmap(X_train.corr(), annot=True)
plt.show()



### 데이터 상태 핸들링 - train 데이터 취합

# X_train과 y_train을 분리해 제공할 경우를 대비해 조인을 일부러 다루어 봤어요
train = X_train.join(y_train.set_index("Serial No."), on="Serial No.")
train.head(3)

# 타겟 데이터와의 상관관계
train[train.columns[1:]].corr()["Chance of Admit "].sort_values(ascending=False)


### 전처리

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_train.iloc[:,1:] = scaler.fit_transform(X_train.iloc[:,1:])
# X_test.iloc[:,1:] = test_ss = scaler.transform(X_test.iloc[:,1:])



### 모델링
# 밸리데이션 데이터를 나누기엔 데이터 자체가 너무 작아 크로스밸리데이션만 확인했었음.

### **(1) 선형회귀 :** `0.7793443258102183`

# 선형회귀 모델
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

from sklearn.model_selection import cross_val_score
scores = cross_val_score(lr, X_train.iloc[:,1:] , y_train["Chance of Admit "] , scoring='r2', cv=5)
print(scores)
print(scores.mean())
#0.7793443258102183


### (2) 랜덤포레스트 : `0.735532640585703`

# 랜덤포레스트
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=2022)

scores = cross_val_score(rf, X_train.iloc[:,1:] , y_train["Chance of Admit "] , scoring='r2', cv=5)
print(scores)
print(scores.mean())
# 0.735532640585703



### 선형회귀 모델 선택 및 예측

# 선형회귀 모델
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train.iloc[:,1:], y_train["Chance of Admit "])
pred = model.predict(X_test.iloc[:,1:])
pred



### 내보내기
# to_csv
pd.DataFrame({'id': X_test['Serial No.'], 'target': pred}).to_csv('003000000.csv', index=False)

# output check
# pd.read_csv("003000000.csv")
