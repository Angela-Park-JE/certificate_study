# 617 JungEun : 230608 THU mission 22 (1)
# 2th type2 - 깍두기
# 전자상거래 데이터 - 제시간 배송 완료 여부 예측

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
    
df = pd.read_csv("../input/customer-analytics/Train.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Reached.on.Time_Y.N', id_name='ID')

X_train.shape, X_test.shape, y_train.shape, y_test.shape



# ---

# EDA baseline에서 추가한 것 ---

temp = pd.concat([X_train, y_train.drop(columns = 'ID')], axis = 1)
temp.corr()



# 데이터 전처리 ---
# object 컬럼은 삭제하지 않고 라벨인코딩을 진행하기로 함
# 합치기
df = pd.concat([X_train, X_test])
df.shape

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder

cols = df.select_dtypes(include = "object").columns
le = LabelEncoder()

for col in cols:
    df[col] = le.fit_transform(df[col])

# 추가로 한 것 minmax 스케일링: 'Cost_of_the_Product', 'Weight_in_gms' 컬럼에 대하여 일부 수정.
from sklearn.preprocessing import minmax_scale as mmscaler
# df.head(3)
df['Cost_of_the_Product'] = mmscaler(df['Cost_of_the_Product'])
df['Weight_in_gms'] = mmscaler(df['Weight_in_gms'])
# df.head(3)

# train test 다시 분리
X_train = df[:X_train.shape[0]].copy()
X_test = df[X_train.shape[0]:].copy()

# shape 확인 : ((8799, 11), (2200, 11), (8799, 2), (2200, 2))
X_train.shape, X_test.shape



# 모델 및 평가 ---
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# 쓸모없는 녀석은 지워둔다.
X_train_id = X_train.pop('ID')
X_test_id = X_test.pop('ID')

from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train['Reached.on.Time_Y.N'], test_size=0.2,random_state=2023)

# 평가지표 
from sklearn.metrics import roc_auc_score


# 1. 로지스틱회귀모델
model = LogisticRegression(random_state = 2023)
model.fit(X_tr, y_tr)
pred = model.predict_proba(X_val)
roc_auc_score(y_val, pred[:,1])     # 0.7272277899340606


# 2. KNN 분류모델
model = KNeighborsClassifier()
model.fit(X_tr, y_tr)
pred = model.predict_proba(X_val)
roc_auc_score(y_val, pred[:,1])     # 0.700657916829534


# 3. 의사결정나무 분류모델
model = DecisionTreeClassifier(random_state = 2023)
model.fit(X_tr, y_tr)
pred = model.predict_proba(X_val)
roc_auc_score(y_val, pred[:,1])     # 0.6514981779008181


# 4. 랜덤포레스트 분류모델
model = RandomForestClassifier(random_state = 1004)
model.fit(X_tr, y_tr)
pred = model.predict_proba(X_val)
roc_auc_score(y_val, pred[:,1])     # 0.7467980619795801

# 5. XGboost 분류모델
model = XGBClassifier(eval_metric = 'mlogloss', use_label_encoder = False, random_state = 2023)
model.fit(X_tr, y_tr)
pred = model.predict_proba(X_val)
roc_auc_score(y_val, pred[:,1])

# 6. +a : LightGBM 분류모델
import lightgbm as lgb

model = lgb.LGBMClassifier(num_leaves = 32, objective = 'binary', random_state = 2023)
model.fit(X_tr, y_tr)
pred = model.predict(X_val)
roc_auc_score(y_val, pred)      # 0.687263842379354

# 7. +a : SVC
from sklearn.svm import SVC

model = SVC(random_state = 2023)
model.fit(X_tr, y_tr)
pred = model.predict(X_val)
roc_auc_score(y_val, pred)      # 0.6992280424623659



# 모델 선정 및 익스포트 ---
model = RandomForestClassifier(random_state = 1004)
model.fit(X_train, y_train['Reached.on.Time_Y.N'])
pred = model.predict_proba(X_test)
# pred

submission = pd.DataFrame({
        "ID": X_test_id,
        "Reached.on.Time_Y.N": pred[:,1]})

# submission.head()
# submission.to_csv('submission.csv', index = False)



# 결과 채점
# 검증데이터(val)보다 조금 떨어진 성능을 보여주고 있음
pred = model.predict_proba(X_test)
roc_auc_score(y_test['Reached.on.Time_Y.N'], pred[:,1])     # 0.7247158076521643
