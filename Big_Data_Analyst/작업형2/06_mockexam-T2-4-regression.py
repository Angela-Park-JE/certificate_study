# 617 JungEun : 230609 FRI mission 23 (1) 
# T2-4 Regression - 깍두기
# 집 값 예측 - 예측할 변수 ['SalePrice']
# 	평가: rmse, r2
# 	rmse는 낮을 수록 좋은 성능
# 	r2는 높을 수록 좋은 성능


# 시험환경 세팅 (코드 변경 X)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def exam_data_load(df, target, id_name="", null_name=""):
    if id_name == "":
        df = df.reset_index().rename(columns={"index": "id"})
        id_name = 'id'
    else:
        id_name = id_name
    
    if null_name != "":
        df[df == null_name] = np.nan
    
    X_train, X_test = train_test_split(df, test_size=0.2, random_state=2021)
    
    y_train = X_train[[id_name, target]]
    X_train = X_train.drop(columns=[target])

    
    y_test = X_test[[id_name, target]]
    X_test = X_test.drop(columns=[target])
    return X_train, X_test, y_train, y_test 
    
df = pd.read_csv("../input/house-prices-advanced-regression-techniques/train.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='SalePrice', id_name='Id')

X_train.shape, X_test.shape, y_train.shape, y_test.shape



# 1. 데이터 불러오기
import pandas as pd

# 확인
X_train.shape, X_test.shape

# 모든 컬럼 불러오기
pd.set_option("display.max_columns", 100)
display(X_train.head(3))
display(X_test.head(3))

# 결측치 확인
X_train.isnull().sum().sort_values(ascending = False)[:20]
X_test.isnull().sum().sort_values(ascending = False)[:20]

# 컬럼 타입 확인
X_train.info()



# 2. 전처리
# 오브젝트 타입 모두 드랍
X_train = X_train.select_dtypes(exclude = ['object'])
X_test = X_test.select_dtypes(exclude = ['object'])
target = y_train['SalePrice']

# 아이디값 따로 옮겨놓기
X_train_id = X_train.pop('Id')
X_test_id = X_test.pop('Id')

# 확인
X_train.head(1)

# Simple imputer : 숫자형 데이터에 대해 채워주는 아이
# 디폴트 값은 mean
from sklearn.impute import SimpleImputer
imp = SimpleImputer()
X_train = imp.fit_transform(X_train)
X_test = imp.transform(X_test)

# validation 데이터 떼어놓기 : ((992, 36), (176, 36), (992,), (176,))
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(X_train, target, test_size = 0.15, random_state=2022)
X_tr.shape, X_val.shape, y_tr.shape, y_val.shape



# 3. 모델링
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_tr, y_tr, verbose = False)
pred = model.predict(X_val)

from sklearn.metrics import mean_squared_error, r2_score

def rmse(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))

print("RMSE : " + str(rmse(y_val, pred)))
print("R2 : " + str(r2_score(y_val, pred)))

# RMSE : 31827.55779287209
# R2 : 0.8534731687038711




### + 간단한(?) 전처리 과정을 거친 것 ---
X_train, X_test, y_train, y_test = exam_data_load(df, target = 'SalePrice', id_name = 'Id')

# 일부 극단치 제거
idx1 = y_train['SalePrice'].quantile(0.005) > y_train['SalePrice']
idx2 = y_train['SalePrice'].quantile(0.995) < y_train['SalePrice']

y_train = y_train[~(idx1 + idx2)]
X_train = X_train[~(idx1 + idx2)]


# 범주형 피처 드랍
X_train = X_train.select_dtypes(exclude = ['object'])
X_test = X_test.select_dtypes(exclude = ['object'])
target = y_train['SalePrice']
X_train_id = X_train.pop('Id')
X_test_id = X_test.pop('Id')


# simple imputer
imp = SimpleImputer()
X_train = imp.fit_transform(X_train)
X_test = imp.transform(X_test)

X_tr, X_val, y_tr, y_val = train_test_split(X_train, target, test_size = 0.15, random_state = 2023)


# 모델 만들기
model = XGBRegressor()
model.fit(X_tr, y_tr)
pred = model.predict(X_val)

print("RMSE : " + str(rmse(y_val, pred)))
print("R2 : " + str(r2_score(y_val, pred)))

# RMSE : 24836.4263305329
# R2 : 0.9052458987853741




### 간단한 모델 튜닝을 거친 것 ---
model = XGBRegressor(n_estimators = 100, max_depth = 4, colsample_bytree = 0.9)
model.fit(X_tr, y_tr)
pred = model.predict(X_val)

print("RMSE : " + str(rmse(y_val, pred)))
print("R2 : " + str(r2_score(y_val, pred)))

# RMSE : 23887.771366900124
# R2 : 0.91234613478725
