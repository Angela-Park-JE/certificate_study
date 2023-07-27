# 617 JungEun : 230614 WED mission 27 (2)
# T2-3 도전
# 깍두기 된 부분: 결과 가져오는 부분, 채점부분만 풀이 참고

# 1, 데이터, 라이브러리 로드
import pandas as pd
import numpy as np



# 2. 데이터 정보 확인
X_train.info()
y_train.info()

y_train['income'].value_counts()

X_train.describe(include = 'object')
X_train.describe(include = 'int64')
X_test.describe(include = 'object')

# train, test 내 오브젝트 컬럼의 unique 값 개수 동일한지 확인하기
pd.DataFrame([X_train.describe(include = 'object').loc['unique'], X_test.describe(include = 'object').loc['unique']])

X_train['occupation'].value_counts()
X_train['workclass'].value_counts()




# 3.결측 확인 : 결측인 항목들이 다 object 타입
# 'native.country'컬럼 : 상대적으로 결측은 적지만 의미있는 라벨인코딩을 위해서는 도메인 지식 필요. 다만 5% 내외이기 때문에 시간적 여유가 있다면 클러스터링을 통해 라벨을 먹이는 것이 가능해보임
# 'occupation' 컬럼 : 클래스간 불균형이 없지는 않지만 다른 컬럼(특히 나라, 소득-예측값, 종사유형)으로 유추 가능해 보임
# 'workclass' 컬럼 : 이 또한 occupatio과 같은 결론
# 아무튼 라벨인코딩이 괜찮을 데이터인지 확인할 수 있는 경력이 못되므로
# 원핫인코딩을 하면 좋겠지만
# 가중치를 ((1/범주수-1)*(1/컬럼수)) 줄 능력이 못되어
# 간단하게 다 드랍하기로.
print(X_train.isna().sum(), '\n') # workclass : 1456 | occupation : 1463 | native.country : 461
print(X_test.isna().sum()) # workclass : 380 | occupation : 380 | native.country : 122



# 4. 전처리

# 4-1. object 컬럼 선택적 드랍
# X_train.describe(include = 'object').columns
# ['workclass', 'education', 'marital.status', 'occupation', 'relationship', 'race', 'sex', 'native.country']
# 성별 컬럼은 컬럼 하나로 원핫인코딩 가능하니까 그대로 둠

df = pd.concat([X_train, X_test], axis = 0)
print(df.shape)

df = df.drop(columns = ['workclass', 'education', 'marital.status', 'occupation', 'relationship', 'race', 'native.country'])
print(df.shape)


# 4-2. 성별컬럼 더미화
# 여성이 남성의 50% 정도로 적으므로 여성이 1이 되도록 하겠음
df['sex'] = df['sex'].replace('Male', 0).replace('Female', 1)
print(df['sex'].value_counts())

# 4-3. target 데이터 더미화
# 카테고리형을 수치로 변환, replace로 income이 무엇인지에 따라 값이 변하도록 함
y_train['target'] = np.nan
y_train['target'] = y_train['income'].replace('<=50K', 0).replace('>50K', 1)
print(y_train['target'].value_counts())


# 4-5. 이상치 핸들링 - 스케일링
# 버리지 않고 최대한 쓰는 방향으로 할 예정
# 'capital.gain', 'capital.loss' 이 스케일 차이가 너무 많이남.
# age, education.num, hours.per.week은 다음 과정에서.
df.describe()
# # 'capital.gain' 90%도 0.0이다. 그렇다면 1이 넘는 것은? 2천여개 대충 10퍼센트 정도. 이상치라고 보기에는 또 많은 수이기도 하다.
# # df['capital.gain'].quantile(0.90)
# # df[df['capital.gain']== 99999.000000] # 이게 159로우나 된다.
# # 통쨰로 스케일링 하는게 나쁜 건 아니지만 그렇게 하기에는 큰 값이 큰 값을 갖는 이유를 잃어버릴 지도 모른다.

# # 이 둘을 각각 민맥스 스케일링을 했을 때 어떨까
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# scaler.fit(df[['capital.gain']])
# df['cg_mms'] = scaler.transform(df[['capital.gain']])
# scaler = MinMaxScaler()
# scaler.fit(df[['capital.loss']])
# df['cl_mms'] = scaler.transform(df[['capital.loss']])
# df.describe()
# # 위 describe()의 결과를 보니 mms의 평균이 더 높아지면서 cg의 의미가 cl보다 낮아질 가능성이 있다.

# dir(sklearn.preprocessing)
# 그래서 이친구들은 표준정규화로 하기로 했음
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df[['capital.gain']])
df['cg_sts'] = scaler.transform(df[['capital.gain']])
scaler = StandardScaler()
scaler.fit(df[['capital.loss']])
df['cl_sts'] = scaler.transform(df[['capital.loss']])
# df.describe()
df = df.drop(columns = ['capital.gain', 'capital.loss'])


# 4-7. 스케일링
# age, education.num, hours.per.week에 대해서는 최소최대 스케일링을 하려 한다.
from sklearn.preprocessing import MinMaxScaler
l = ['age', 'education.num', 'hours.per.week']
for i in l:
    scaler = MinMaxScaler()
    scaler.fit(df[[i]])
    ss = scaler.transform(df[[i]])
    df[i] = ss
df.describe()


# 4-8. 데이터 분할
X_tr = df[:X_train.shape[0]]
X_te = df[X_train.shape[0]:]
y_tr = y_train[['id', 'target']]
X_train.shape, X_tr.shape, X_test.shape, X_te.shape


# 4-9. id 컬럼 드랍 및 확인
id_tr = X_tr.pop('id')
id_te = X_te.pop('id')
X_tr.info()



# 5. 모델링 : 실력이 아직 안되니 validation 데이터 만들기는 내일 외워서 내일부터 제대로 쓰기로
# import sklearn.ensemble
# dir(sklearn.ensemble) # GradientBoostingClassifier,RandomForestClassifier, StackingClassifier 

# 5-1. GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingClassifier
model1 = GradientBoostingClassifier(max_depth = 4, random_state = 617, max_leaf_nodes = 41)
model1.fit(X = X_tr, y = y_tr['target'])
gbc_pred = model1.predict(X_te)
# gbc_pred


# 5-2. RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
model2 = RandomForestClassifier(max_depth = 4, random_state = 617, max_leaf_nodes = 41)
model2.fit(X = X_tr, y = y_tr['target'])
rfc_pred = model2.predict(X_te)
# rfc_pred


# # 5-3. StackingClassifier : 되긴 되나 50초 넘어가서 실패
# from sklearn.ensemble import StackingClassifier
# from sklearn.svm import SVC
# estimators = [
#             ('gbc', GradientBoostingClassifier(max_depth = 4, random_state = 617, max_leaf_nodes = 41)),
#             ('rfc', RandomForestClassifier(max_depth = 4, random_state = 617, max_leaf_nodes = 41)),
#             ('svr', SVC(random_state = 617))]
# model3 = StackingClassifier(estimators = estimators, cv = 5)
# model3.fit(X = X_tr, y = y_tr['target'])
# stck_pred = model3.predict(X_te)
# stck_pred



# 6. 결과 디코딩 및 형식 맞추기
# s_gbc_pred = pd.Series(gbc_pred).replace(0, '<=50K').replace(1, '>50K')
# s_rfc_pred = pd.Series(rfc_pred).replace(0, '<=50K').replace(1, '>50K')
# 이러고 있었는데 확인해보니까 바꿀 필요가 없었다.
# 저장에서 애먹어서 일단 이부분부터는 풀이 참고함

# 그냥 그대로 쓰기로
output = pd.DataFrame({'id': id_te, 'income':gbc_pred})
output.to_csv("gbc_617.csv", index = False)
output = pd.DataFrame({'id': id_te, 'income':rfc_pred})
output.to_csv("rfc_617.csv", index = False)
output.shape



# END!!!!!!!!!! 채점
y_test = (y_test['income'] != '<=50K').astype(int)
from sklearn.metrics import accuracy_score
print('accuracy score:', (accuracy_score(y_test, gbc_pred)))
print('accuracy score:', (accuracy_score(y_test, rfc_pred)))

# RESULTS
# accuracy score: 0.8549055734684478
# accuracy score: 0.8326424074927069
