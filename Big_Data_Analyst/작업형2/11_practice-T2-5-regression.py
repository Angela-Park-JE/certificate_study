# 617 JungEun : 230615 THU mission 28 (2)
# T2-5 도전
# 깍두기 된 부분: 결과 가져오는 부분, 채점부분만 풀이 참고
# 보험료 맞추기


# 컬럼 확인
print(X_train.shape, y_train.shape, X_test.shape)
print(X_train.info())

# target 확인
y_train



# EDA - 결측치 체크 : 없음
print(X_train.isnull().sum(), '\n')
print(X_test.isnull().sum())


# 합쳐서 보기 및 수정 준비
df = pd.concat([X_train, X_test], axis = 0)



# EDA - object 타입 : 'sex' 이진, 'smoker' 이진, 'region' 4가지 -> 인코딩 의미 있어 보임
obj_list = list(df.select_dtypes(include = 'object').columns)
for i in obj_list:
    print(df[i].value_counts())



# Preprocessing - object 타입 이진 컬럼 만들기
# 'sex' : female 이 조금 더 적으므로 1로 만들기
df.loc[:, 'sex'] = (df['sex'] == 'female').astype('int')

# 'smoker' : yes 가 더 적으므로 1로 만들기
df.loc[:, 'smoker'] = (df['smoker'] == 'yes').astype('int')



# # Preprocessing - object 타입 원핫인코딩 
# # 'region' : 범주가 4개로 많지는 않은 편으로 원핫인코딩을 진행함
# # 처음에 pd.get_dummies 했어야했는데 df에 하면서 왜안되냐고 당황하고 불러왔던 사이킷런 원핫인코더. 이마저도 제대로 못해서 수작업으로.

# from sklearn.preprocessing import OneHotEncoder
# encoder = OneHotEncoder(drop = 'first')
# encoder.fit(df[['region']])
# region_encoded = encoder.transform(df[['region']])
# region_encoded  # 이 결과를 어떻게 불러오질 못해어 수작업으로 함


# 첫번째 northeast는 드랍하고 나머지 범주를 각 맞게 0 혹은 1로 넣기로 함
region_list = list(df['region'].unique())
region_list = region_list[1:]
# 인코딩 결과를 각 값에 따라 T/F->1/0 넣도록 함.
# 인코딩
for i in region_list:
    s = (df['region'] == i).astype('int')
    df[i] = s

# 원핫 인코딩 결과가 있으므로 남은 원래 object 컬럼 drop
df = df.drop(columns = 'region')
# df



# Preprocessing - 수치형 스케일링 : 'age', 'bmi', 'children' 
# df.describe(exclude = 'object')
from sklearn.preprocessing import MinMaxScaler, RobustScaler

# 'age' : MinMax
scaler = MinMaxScaler()
scaler.fit(df[['age']])
ages = scaler.transform(df[['age']])
df['age'] = ages

# 'bmi' : Robust
scaler = RobustScaler()
scaler.fit(df[['bmi']])
bmis = scaler.transform(df[['bmi']])
df['bmi'] = bmis

# 'children' : MinMax
scaler = MinMaxScaler()
scaler.fit(df[['children']])
childrens= scaler.transform(df[['children']])
df['children'] = childrens
# df



# df 분할 및 특징 정리
X_tr = df[:X_train.shape[0]]
X_te = df[X_train.shape[0]:]
# print(X_train.shape, X_tr.shape, X_test.shape, X_te.shape)

id_tr, id_te = X_tr.pop('id'), X_te.pop('id')



# 모델링

# random forest regression
from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(max_leaf_nodes = 21, random_state = 617, criterion = 'friedman_mse')
rfr.fit(X_tr, y_train['charges'])
rfr_pred = rfr.predict(X_te)
rfr_pred[:5]

# gradient boosting regression
from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor(learning_rate = 0.05, max_leaf_nodes = 31, random_state = 617, validation_fraction = 0.15)
gbr.fit(X_tr, y_train['charges'])
gbr_pred = gbr.predict(X_te)
gbr_pred[:5]

# linear regression (비교용)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lrfit = lr.fit(X_tr, y_train['charges'])
# lrfit.score(X_tr, y_train['charges']) # score by train data 
# lrfit.coef_ # col effection
lr_pred = lr.predict(X_te)
lr_pred[:5]



# 원래대로라면 validation 성적에 따라 모델을 선택하지만
# 나는 일단 응애니까 여기부분은 풀이에서 가져와서 채점을 해보겠다. 내일은 응애그만하자
# rmse, mse 가져오는 것 하기
# 그리고 XGBoost 도 까먹음 ㅎㅎ xgboost 라고 써야했음 ㅎㅎ



# RMSE 산출 및 선정 - 깍두기
from sklearn.metrics import mean_squared_error
def rmse2(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

print(rmse2(y_test['charges'], rfr_pred))
print(rmse2(y_test['charges'], gbr_pred)) # 선정
print(rmse2(y_test['charges'], lr_pred))  # 데이터가 이렇게 작아도 단일로는 역시 무리가 있는 모델

# # 결과
# 4602.525098942823
# 4572.395432930046
# 6069.026921808219




# 결과 제출
pd.DataFrame({'id': X_test.id, 'charges': gbr_pred}).to_csv('617.csv', index = False)
# 확인
# pd.read_csv('/kaggle/working/617.csv')
