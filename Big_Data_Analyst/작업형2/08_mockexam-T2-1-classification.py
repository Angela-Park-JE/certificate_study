# 617 JungEun : 230612 MON mission 25 (4)
# 모의고사1 T2 깍두기
# 확률로 이직 예측하기


# 시험장 제공 안내 코드 생략 --

# 간단한 EDA - dtype, null 체크

print(X_train.shape, y_train.shape, X_test.shape)
print('=====================')
print(X_train.info())
print(y_train.info())
print(X_test.info())
print('=====================')
print(X_train.isna().sum())
print('---------------------')
print(X_test.isna().sum())



# 피처 셀렉팅

# only numbers type : `.select_dtypes(exclude = 'object')`
X_tr = X_train.select_dtypes(exclude = 'object')
X_te = X_test.select_dtypes(exclude = 'object')

# drop id column : `.drop('col', axis =1)`
X_tr = X_tr.drop(columns = 'enrollee_id')
X_te = X_te.drop(columns = 'enrollee_id')
print(X_te.head())



# 모델링

# (1) 기본 제공 - rf : 0.6638704077060932
# Training
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state = 2023)
model.fit(X_tr, y_train['target'])
pred = model.predict_proba(X_te)[:, 1]    # [0]은 0일 확률 1은 1일 확률이라고 보면 된다 합해서 1이됨, 이직할 사람이 1.

# (2) svc 해본것 : 채점(rocauc)은 정확히 0.5였음. 그냥 랜덤포레스트 쓰자.
import sklearn.svm
# print(dir(sklearn.svm))
# Training
from sklearn.svm import SVC
model = SVC(probability = True, random_state = 2023)
model.fit(X_tr, y_train['target'])
pred = model.predict(X_te) # 아웃풋이 0일확률과 1일확률로 나눠지지 않고 1차원으로 나옴


# (3) gradiant boosting cls 해본것 : 0.7173023073476702
# Training
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(random_state = 2023)
model.fit(X_tr, y_train['target'])
pred = model.predict_proba(X_te)[:, 1]



# 내보내기
# to_csv (제공되는 코드를 복사하기)
pd.DataFrame({'enrollee_id': X_test.enrollee_id, 'target': pred}).to_csv('617.csv', index = False)

# output check
# pd.read_csv('/kaggle/working/617.csv')
