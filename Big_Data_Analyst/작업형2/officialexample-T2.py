# 공식 예시문제 유형 2 깍두기
# 617 JungEun : 230605 MON mission 19 (1)

# 유형 2
# 1. Libraries and dataset load
import pandas as pd
path = "../input/departmentstorecustomer/"
X = pd.read_csv(path + "X_train.csv", encoding = "euc-kr") 
y = pd.read_csv(path + "y_train.csv")
test = pd.read_csv(path + "X_test.csv", encoding = "euc-kr")



# 2. EDA
# X.shape, y.shape, test.shape

# null check
# X.isnull().sum()

# X_train 데이터 기초통계 
# X.describe()
# X.describe(include = 'object')

# X_test 데이터 기초통계 
test.describe()
X.describe(include = 'object')

# label값 확인 
y['gender'].value_counts()



# 3. Preprocessing
# 결측치처리
X = X.fillna(0) # 환불금액 0값으로 채움
test = test.fillna(0)

X = X.drop(['cust_id'], axis=1)
cust_id = test.pop('cust_id')



# 4. Feature Engineering
# Label Encoding 
from sklearn.preprocessing import LabelEncoder
cols = ['주구매상품', '주구매지점']
for col in cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    test[col] = le.transform(test[col])

# X.head()



# 5. Modeling, Hyperparameter tuning, Ensemble

# random forest - classifier
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 100, max_depth = 5, random_state = 2022)
model.fit(X, y['gender'])
print(model.score(X, y['gender']))
predictions = model.predict_proba(test)

# check
predictions[:,1]



# 6. result handling
# csv file 생성
output = pd.DataFrame({'cust_id': cust_id, 'gender': predictions[:,1]})

# 생성할 것 체크
# output.head()

# 생성
output.to_csv("123456789.csv", index = False)

# 생성된 것 체크
# pd.read_csv("123456789.csv")
