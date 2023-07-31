# 617 JungEun : 230614 FRI mission 29 (2)
# T2-6 도전
# 깍두기 된 부분: 검증데이터, r2_score의 의미

# 라이브러리 및 타겟 데이터 분할
import pandas as pd

sub_sample = pd.read_csv('/kaggle/input/bike-sharing-demand/sampleSubmission.csv')
test = pd.read_csv('/kaggle/input/bike-sharing-demand/test.csv')
train = pd.read_csv('/kaggle/input/bike-sharing-demand/train.csv')

y_tr = train.pop('count')


# 데이터 확인
# train.columns
# test.columns # (casual, registered 가 없다) 최종적으로 
print(train.shape, test.shape)
train.head()
sub_sample.head() # 시간대 별로 count 해야한다.


# 데이터 타입 확인 : 이제 시간이 되는 datetime 열 외에는 타입을 만질만한 부분은 없어보인다.
# 다만 season과 weather는 범주형 카테고리인데 숫자 타입으로 나누어져 있는 것을 알 수 있다.
print(train.info())
print(test.info())



# 1. 데이터 정리
# (1) 데이터 타입 변경
train['datetime'] = pd.to_datetime(train['datetime'])
test['datetime'] = pd.to_datetime(test['datetime'])

# (2) count target 데이터 생성 (전날 하면서 pop으로 빼놓고 왜 없지 하면서 만들었던 부분)
train['count'] = train['casual'] + train['registered']
y_tr = train[['datetime', 'count']]
X_tr = train.drop(columns = ['casual', 'registered', 'count'])
X_tr.head(5)

# (3) 테스트 데이터도 확인
# test.head()
X_te = test
print(X_tr.shape, X_te.shape)
X_te.head()



# 2. 전처리 - X_tr와 X_te 에서의 결측치 확인
X_tr.isna().sum() # 없음
X_te.isna().sum() # 없음

# 2. 전처리 - 이상치 탐색
# 풍속 외에는 특별한 이상치는 발견되지 않는 것으로 보임. 
# season과 weather는 onehotencoding 필요해보임
X_tr.describe()

# 풍속 보기 : 기계가 측정할 수 있는 최대 풍속으로 측정된 듯 하다. 가장 큰 값으로 0703일 17시와 18시에 있다
X_tr.sort_values('windspeed', ascending = False)

# 계절 컬럼 : 1(1~3월), 2(4~6월), 3(7~9월), 4(10~12월)로 되어있다.
seasons = [1, 2, 3, 4]
for i in seasons:
    print(X_tr[X_tr['season'] == i][:2])

# 계절을 나눈 것이 계절이라고 하기엔 그냥 quarter 같은데 
# 그룹바이 하여 분기로 나누는 게 좋을 지, 우리나라 계절처럼 나누는 게 좋을지 비교해보려 한다. 
# 보는건 평균과 분산을 볼 것이다.
# 만약 후자가 좋다면 계절컬럼을 test 데이터도 함께 변경해서 바꾸고자한다.
# (1) 계절 컬럼 그대로 평균
pd.pivot_table(data = X_tr, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'mean')

# (2) 계절 컬럼 그대로 분산
pd.pivot_table(data = X_tr, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'var')

# (3) 계절 컬럼을 바꾸었을때 평균 : 시리즈.isin(['a','b']) 사용
# 계절별로 바꿈 봄부터 1, 2, 3 ,4 (개월이 하나씩 땡겨진 것.)
sp = X_tr[X_tr['datetime'].dt.month.isin([3,4,5])]
sp.loc[:,'season'] = 1
su = X_tr[X_tr['datetime'].dt.month.isin([6,7,8])] 
su.loc[:,'season'] = 2
au = X_tr[X_tr['datetime'].dt.month.isin([9,10,11])] 
au.loc[:,'season'] = 3
wi = X_tr[X_tr['datetime'].dt.month.isin([12,1,2])] 
wi.loc[:,'season'] = 4

# new DF
X_tr_editseason = pd.concat([sp, su, au, wi], axis = 0)
pd.pivot_table(data = X_tr_editseason, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'mean')

# (4) 계절 컬럼을 바꾸었을때 분산
pd.pivot_table(data = X_tr_editseason, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'var')

# (5) 분산 비교 : 바꾼 것에서 이전 것을 뺐으므로 음수가 많을 수록 이전 것의 분산이 더 크며 계절구분 안에서의 데이터 분산이 크다는 말. 
# 즉 해당 카테고리가 덜 적절하다는 말. 3에서는 오히려 이전 것이 나은 것을 보여줬다. 3은 이전것은 7,8,9월이며, 내것은 9,10,11 이다. 
# 2의 경우 내것이 훨씬 나은 것도 보여주었다. 2는 이전것은 4,5,6 월, 내것은 6,7,8이다. 
var1 = pd.pivot_table(data = X_tr, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'var')
var2 = pd.pivot_table(data = X_tr_editseason, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'var')

var2-var1


# 만약 2는 6,7,8,9를 이용하되 3은 10, 11/ 4는 12, 1, 2/ 1은 3,4,5 를 한다면 어떨까

sp = X_tr[X_tr['datetime'].dt.month.isin([3,4,5])]
sp.loc[:,'season'] = 1
su = X_tr[X_tr['datetime'].dt.month.isin([6,7,8,9])] 
su.loc[:,'season'] = 2
au = X_tr[X_tr['datetime'].dt.month.isin([10,11])] 
au.loc[:,'season'] = 3
wi = X_tr[X_tr['datetime'].dt.month.isin([12,1,2])] 
wi.loc[:,'season'] = 4

# new DF
X_tr_editseason = pd.concat([sp, su, au, wi], axis = 0)

var1 = pd.pivot_table(data = X_tr, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'var')
var2 = pd.pivot_table(data = X_tr_editseason, index = 'season', values = ['weather', 'temp', 'atemp', 'humidity', 'windspeed'], aggfunc = 'var')

var2-var1

# 3시즌의 이전 분산이 더 작았던 것을 보완하였다. 습도의 경우 조금 더 커졌으나 분산이라 저정도 큰 것은 괜찮을 것이라는 생각이 든다.


# 2. 전처리 - 전처리 위해 tr,te 데이터 병합

df = pd.concat([X_tr, X_te], axis = 0)
# df

# 여기서 시즌 부분을 변경했으나 의미 없게 되어 나중에 다시 해볼때는 하지 않을 과정.
# 2. 전처리 - 시즌 부분 변경

sp = df[df['datetime'].dt.month.isin([3,4,5])]
sp.loc[:,'season'] = 1
su = df[df['datetime'].dt.month.isin([6,7,8,9])] 
su.loc[:,'season'] = 2
au = df[df['datetime'].dt.month.isin([10,11])] 
au.loc[:,'season'] = 3
wi = df[df['datetime'].dt.month.isin([12,1,2])] 
wi.loc[:,'season'] = 4

df = pd.concat([sp, su, au, wi], axis = 0)
df = df.sort_index()
df


# 1은 맑거나 구름, 2는 안개, 3은 약간의 눈이나 비 천둥, 4는 폭우, 우박, 눈이 오면서 안개 (악천후)
# weather - 
# 1: Clear, Few clouds, Partly cloudy, Partly cloudy
# 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
# 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
# 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog 

# 2. 전처리 - 시즌, 날씨 원핫 인코딩
# pd.get_dummies(df, columns = ['season', 'weather'], drop_first = True) # 잘 나온 것을 확인할 수 있음
df = pd.get_dummies(df, columns = ['season', 'weather'], drop_first = True)

# 2. 전처리 - 스케일링
# 스케일링 전의 상관관계는 어떨까 (season이 원핫 더미로 뒤로 갔기 때문에 holiday부터)
df2 = pd.concat([df.loc[:X_tr.shape[0], :], y_tr], axis = 1)
df2.loc[:, 'holiday':].corr().loc[:, 'count']

# 2. 전처리 - 스케일링 : temp	atemp	humidity	windspeed
from sklearn.preprocessing import *
mms = MinMaxScaler()
rbs = RobustScaler()
# sts = StandardScaler() # 나중에 성능 비교하고 싶을 떄 사용해보기로

# temp와 atemp는 robust
# humidity와 windspeed는 minmax 진행

df.loc[:, 'temp'] = rbs.fit_transform(df[['temp']])
df.loc[:, 'atemp'] = rbs.fit_transform(df[['atemp']])
df.loc[:, 'humidity'] = mms.fit_transform(df[['humidity']])
df.loc[:, 'windspeed'] = mms.fit_transform(df[['windspeed']])
df



# 3. 데이터 나누고 피처셀렉팅 준비
X_tr = df[:X_tr.shape[0]]
X_te = df[X_tr.shape[0]:]

# 상관관계 구해보기
df_with_y = X_tr.copy()
df_with_y.loc[:, 'count'] = y_tr['count']
df_with_y.loc[:, 'holiday':].corr().loc[:, 'count']
# 재미있는 건 건드리지 않은 것들도 상관관계가 변했다는 것이다.

print(X_tr.shape, X_te.shape, y_tr.shape)

trdatetime = X_tr.pop('datetime')
tedatetime = X_te.pop('datetime')



# 4. validation 데이터 나누기
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X_tr, y_tr, test_size = 0.2, random_state = 617)
X_train.shape, X_val.shape, y_train.shape, y_val.shape



# 5. 모델링 - 3개 모델
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

## (1) [월, 시간대 분리 X | 스케일링 뒤] 모델링
# 랜덤 포레스트

rfr = RandomForestRegressor(random_state = 617)
rfr.fit(X_train, y_train['count'])
pred_rfr = rfr.predict(X_val

# 그래디언트부스트 회귀

gbr = GradientBoostingRegressor(random_state = 617)
gbr.fit(X_train, y_train['count'])
pred_gbr = gbr.predict(X_val)

# XGBoost

xgr = XGBRegressor(random_state = 617, learning_rate = 0.01)
xgr.fit(X_train, y_train['count'])
pred_xgr = xgr.predict(X_val)


# [월, 시간대 분리 X | 스케일링 뒤] 모델 평가
# 랜덤포레스트 결과
from sklearn.metrics import mean_squared_error, r2_score
print('rfr:', (mean_squared_error(y_val['count'], pred_rfr))**0.5)
print('gbr:', (mean_squared_error(y_val['count'], pred_gbr))**0.5)
print('xgr:', (mean_squared_error(y_val['count'], pred_xgr))**0.5)

# rfr: 183.76257990090116
# gbr: 179.67349600936686
# xgr: 192.7253637275508

print(r2_score(y_val['count'], pred_rfr)) # -0.01206025967182578
# 음수가 나왔다. 모든 변수를 평균으로 넣었을 때 보다 정확도가 떨어진단 소리다. 완전 망한 모델.
print(r2_score(y_val['count'], pred_gbr)) # 0.03247933580288831
print(r2_score(y_val['count'], pred_xgr)) # -0.11319170360233177
# 더 망한 모델이 있었네


## (2) [월, 시간대 분리 O | 스케일링 뒤] 모델 준비
df2 = df.copy()
df2['month'] = df['datetime'].dt.month
df2['hour'] = df['datetime'].dt.hour

X_tr = df[:X_tr.shape[0]]
X_te = df[X_tr.shape[0]:]

trdatetime = X_tr.pop('datetime')
tedatetime = X_te.pop('datetime')

# validation 데이터 나누기
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_tr, y_tr, test_size = 0.2, random_state = 617)
X_train.shape, X_val.shape, y_train.shape, y_val.shape

# [월, 시간대 분리 O | 스케일링 뒤] 모델링
# 랜덤 포레스트
rfr = RandomForestRegressor(random_state = 617)
rfr.fit(X_train, y_train['count'])
pred_rfr = rfr.predict(X_val)

# 그래디언트부스트 회귀
gbr = GradientBoostingRegressor(random_state = 617)
gbr.fit(X_train, y_train['count'])
pred_gbr = gbr.predict(X_val)

# XGBoost
xgr = XGBRegressor(random_state = 617, learning_rate = 0.01)
xgr.fit(X_train, y_train['count'])
pred_xgr = xgr.predict(X_val)


# [월, 시간대 분리 O | 스케일링 뒤] 모델 평가
# 랜덤포레스트 결과 
from sklearn.metrics import mean_squared_error
print('rfr:', (mean_squared_error(y_val['count'], pred_rfr))**0.5)
print('gbr:', (mean_squared_error(y_val['count'], pred_gbr))**0.5)
print('xgr:', (mean_squared_error(y_val['count'], pred_xgr))**0.5)

# 전
# rfr: 183.76257990090116
# gbr: 179.67349600936686
# xgr: 192.7253637275508
# 후
# rfr: 182.37274849604256
# gbr: 175.09604162344004
# xgr: 189.84164198742985

print(r2_score(y_val['count'], pred_rfr)) # -0.01206025967182578 -> -0.0454576799601214 더 망함
print(r2_score(y_val['count'], pred_gbr)) # 0.03247933580288831 -> 0.036305840363573205 아주 약간 나아짐
print(r2_score(y_val['count'], pred_xgr)) #-0.11319170360233177 -> -0.13284250011319587 더 망함





# 최종 모델링
# (3) [월, 시간대 분리 O | 전처리 전, 스케일링 전] 모델 모델링 전 과정

# 데이터 불러오기
train = pd.read_csv("/kaggle/input/bike-sharing-demand/train.csv", parse_dates = ['datetime'])
test = pd.read_csv("/kaggle/input/bike-sharing-demand/test.csv", parse_dates = ['datetime'])


# train의 'count' 뺴두기
y_train = train.pop('count')


# train의 count가 되는 두 컬럼도 drop
train = train.drop(columns = ['casual', 'registered'])
df = pd.concat([train, test], axis = 0)


# datetime type 분리하기 : 월과 계절이 서로 다중공선성 문제를 일으킬 수도 있다는 생각이 들었으나 계절1 같은 데이터로 막아질 거라는 생각을 했음
df['month'] = df['datetime'].dt.month
df['date'] = df['datetime'].dt.day
df['hour'] = df['datetime'].dt.hour
df = df.drop('datetime', axis = 1)

X_train, X_test = df[:train.shape[0]], df[train.shape[0]:]


# 검증 데이터 나누기
X_tr, X_val, y_tr, y_val  = train_test_split(X_train, y_train, test_size = 0.15, random_state = 617)
# print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)


# 모델링 (GradientBoostingRegressor)
from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor(random_state = 617)
gbr.fit(X_tr, y_tr)
gbr_pred = gbr.predict(X_val)


# r2 score로 확인
from sklearn.metrics import r2_score, mean_squared_error
print('r2:', r2_score(y_val, gbr_pred), '| rmse:', (mean_squared_error(y_val, gbr_pred))**0.5)

# r2: 0.7898731070628514 | rmse: 80.79890119365493



# 최종 예측
pred = gbr.predict(X_test)
# to_csv 
pd.DataFrame({'enrollee_id': test['datetime'], 'target': pred}).to_csv('617.csv', index = False)
# 확인
# pd.read_csv('/kaggle/working/617.csv')
