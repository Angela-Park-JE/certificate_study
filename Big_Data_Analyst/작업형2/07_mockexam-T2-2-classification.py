# 617 JungEun : 230610 SAT mission 24 (1)
# T2-2 Classification : 당뇨병 여부 판단
# 이상치 처리 (Glucose, BloodPressure, SkinThickness, Insulin, BMI가 0인 값)

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
    
df = pd.read_csv("../input/pima-indians-diabetes-database/diabetes.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Outcome')

X_train.shape, X_test.shape, y_train.shape, y_test.shape
# ((614, 9), (154, 9), (614, 2), (154, 2))
# -----




# 1. Data and libraries
import pandas as pd
X_train.shape, y_train.shape, X_test.shape 
# ((614, 9), (614, 2), (154, 9))



# 2. EDA
# X_train.head()
# y_train.value_counts()
# X_train.info()
# X_train.isnull().sum()
# X_test.isnull().sum()

# X_train.describe()



# 3. Preprocessing
#이상치 처리
#Train
print('Glucose:',len(X_train[X_train['Glucose'] == 0]))
print('BloodPressure:',len(X_train[X_train['BloodPressure'] == 0]))
print('SkinThickness:',len(X_train[X_train['SkinThickness'] == 0]))
print('Insulin:',len(X_train[X_train['Insulin'] == 0]))
print('BMI:',len(X_train[X_train['BMI'] == 0]))

# Glucose: 5
# BloodPressure: 31
# SkinThickness: 175
# Insulin: 287
# BMI: 9

#Test
print('Glucose:',len(X_test[X_test['Glucose'] == 0]))
print('BloodPressure:',len(X_test[X_test['BloodPressure'] == 0]))
print('SkinThickness:',len(X_test[X_test['SkinThickness'] == 0]))
print('Insulin:',len(X_test[X_test['Insulin'] == 0]))
print('BMI:',len(X_test[X_test['BMI'] == 0]))

# Glucose: 0
# BloodPressure: 4
# SkinThickness: 52
# Insulin: 87
# BMI: 2

# 트레인에만 0이 있는 포도당(Glucose)는 아예 로우를 삭제. 나머지는 평균값으로 대체 하여 이상치를 처리함
# 포도당 이상치 삭제
del_idx = X_train[(X_train['Glucose'] == 0)].index
# del_idx

# print('Glucose 이상치 삭제 전 :', X_train.shape, y_train.shape)
X_train = X_train.drop(index = del_idx, axis=0)
y_train = y_train.drop(index = del_idx, axis=0)
# print('Glucose 이상치 삭제 후 :', X_train.shape, y_train.shape)

# Glucose 이상치 삭제 전 : (614, 9) (614, 2)
# Glucose 이상치 삭제 후 : (609, 9) (609, 2)

# 포도당을 제외한 이상치, 평균값으로 대체
cols = ['BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
# cols_mean = X_train[cols].mean()
# X_train[cols].replace(0, cols_mean, inplace = True)
for i in range(4):
    cols_mean = X_train[cols[i]].mean()
    X_train[cols[i]] = X_train[cols[i]].replace(0, cols_mean)
 # inplace로 바꾸었더니 카피워닝이 떴음. 그럼뭐 어떡해... for 돌려야지

 # 스케일링
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X_train[cols] = scaler.fit_transform(X_train[cols])
X_test[cols] = scaler.fit_transform(X_test[cols])



# 4. 모델링 전 점검 : validation data 나눠서 테스트 해보기
# # id 제외
# X = X_train.drop('id', axis= 1)
# test = X_test.drop('id', axis= 1)
# 따로 옮기기. 이렇게 써두기로 함.
X_train_id = X_train.pop('id')
X_test_id = X_test.pop('id')

# validation 데이터 떼어놓기 : X_train, X_test, y_train, y_test
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size = 0.15, random_state = 2023)
# X_tr.shape, X_val.shape, y_tr.shape, y_val.shape



# 5. Modeling

# (1) XGBoost Classifier를 써보기로 했다
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_tr, y_tr['Outcome'], verbose = False)
pred = model.predict(X_val)

from sklearn.metrics import roc_auc_score
def rocauc_score(y, y_pred):
    return (roc_auc_score(y, y_pred))
# print("ROC_AUC_SCORE : " + str(rocauc_score(y_val['Outcome'], pred)))
# ROC_AUC_SCORE : 0.7023809523809524



# (2) SVC
from sklearn.svm import SVC
model = SVC(random_state = 2023)
model.fit(X_train, y_train['Outcome'])
predictions = model.predict(X_test)

# 오버피팅 되었을 경우에 점수가 잘나올 수 있음 (객관적인 평가 아님, 밸리데이션 데이터로 평가 필요함)
# round(model.score(X_train, y_train['Outcome']) * 100, 2) 
# train 데이터로 74.55

output = pd.DataFrame({'idx': X_test.index, 'Outcome': predictions})
# output.head()



# 6. 수험번호.csv로 출력
output.to_csv('1212617.csv', index = False)
submission = pd.read_csv('/kaggle/working/1212617.csv')
# submission


# -----
# 수험자는 모르는 테스트
# round(model.score(X_test, y_test['Outcome']) * 100, 2) 
# 최종적으로 73.38 이 나왔다.
