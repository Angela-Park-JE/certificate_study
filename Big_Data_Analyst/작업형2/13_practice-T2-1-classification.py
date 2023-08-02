# 617 JungEun : 230617 SAT mission 30 (2)
# T2-1 도전
# 타이타닉 생존 확률 예측


### 간단한 EDA - dtype, null 체크
# 1. 데이터 인포
X_train.info()

y_train.info()

X_test.info()

y_train['Survived'].value_counts()


# 2. 데이터 요약
X_train.describe()

# 이상치 탐색
# Age 컬럼의 경우 결측치가 많으며, -> 결측은 후에 Name을 처리하여 성씨를 가지고 넣어도 좋을 듯 하다.
# 혹은 간단하게 KNN으로 Age, Pclass와 Fare, Embarked로 추정해도 좋을 듯 하다.
# 아직 그럴 실력이 안되기 때문에 지금은 Embarked별 성별별 평균을 넣도록 해야겠다.

# 아이 ㅇ왜안돼
# 우선 나이가.5로 표시된 사람들에 대해서는 int로 만들며, 1이하의 경우 1로 처리하도록 하는 것이 좋아보인다.
# X_train[(X_train['Age']%1!=0)&(X_train['Age'].isna()!=True)].sort_values(['Age'], ascending = False)
# X_train[(X_train['Age']<1)].loc[:, 'Age'] = 1
# X_train[(X_train['Age']%1!=0)&(X_train['Age'].isna()!=True)].loc[:, 'Age'] = X_train[(X_train['Age']%1!=0)&(X_train['Age'].isna()!=True)].loc[:, 'Age'].astype('int64')
# df[(df['Age']%1!=0)&(df['Age'].isna()!=True)]

# 먼저, 데이터가 너무 적기 때문에 drop은 하지 않을 것이므로 df로 합치기로 한다.
df = pd.concat([X_train, X_test], axis = 0)

# 그리고 성별 별 탑승지별 Pclass 별 평균을 Age에 넣으려고 한다.
# 잘 안돼서 성별 평균 넣으려 함
# dfagemean = df.groupby(['Embarked', 'Pclass', 'Sex'])['Age'].mean()
# dfagemean = dfagemean.reset_index()
# list(dfagemean.iloc[1, :].values)


# age 넣기
dfagemean = df.groupby(['Sex'])['Age'].mean()
dic = dict(zip(list(dfagemean.index), list(dfagemean.values)))

df['Age'].fillna(df['Age'].map(dic), inplace = True)
# df.isna().sum()

df['Age'].fillna(df['Age'].map(dic), inplace = True)
# 177개의 데이터가 매칭이 안되고 남는다
df['Age'].fillna(df['Age'].median(), inplace = True)
# 여기까지 해야 괜찮아진다.
df.isna().sum()


# 전처리 - cabin의 경우 정말 제멋대로이기 때문에 컬럼 자체를 drop 하기로 함
# df['Cabin'].value_counts()
df = df.drop(axis = 1, columns = 'Cabin')
df.isna().sum()


# 전처리 - 'Embarked'의 경우 상선지인데 결측이 2개이므로 최빈값을 넣도록 한다
# df['Embarked'].value_counts()
# S    644
# C    168
# Q     77

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].sort_values(ascending = False)[0])
# df['Embarked'].value_counts()
# S    646
# C    168
# Q     77


# 결측 완. 범주형 수정
# 전처리 - 범주형 중 Name, Ticket은 드랍, Sex는 바이너리로, Embarked는 원핫인코딩을 진행한다.
# Pclass의 경우 범주형의 일부이나, 그대로 가되 성능이 많이 좋지 않을 경우 다시보기로 한다.
objlist = list(df.select_dtypes('O').columns)


# 전처리 - 범주형 드랍
df = df.drop(columns = ['Name', 'Ticket'])


# 전처리 - Sex 컬럼 이진변수화
# df['Sex'].value_counts()
# male      577
# female    314

# 여성이 더 희소하므로 경우 1로 지정
df['Sex'] = (df['Sex'] != 'male').astype(int)
# df['Sex'].value_counts()
# 0    577
# 1    314


# 전처리 - Embarked 원핫 인코딩
df = pd.get_dummies(df, columns = ['Embarked'], drop_first = True)
# df 체크
df.info()
# y_train



### 모델링 준비 - 검증데이터
