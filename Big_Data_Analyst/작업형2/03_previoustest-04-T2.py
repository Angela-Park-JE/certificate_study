# ## **Q. [마케팅] 자동차 시장 세분화**

# - 자동차 회사는 새로운 전략을 수립하기 위해 4개의 시장으로 세분화했습니다.
# - 기존 고객 분류 자료를 바탕으로 신규 고객이 어떤 분류에 속할지 예측해주세요!
# - 예측할 값(y): "Segmentation" (1,2,3,4)
# - 평가: Macro f1-score



# 617 JungEun : 230606 TUE mission 20 (1)
# 4th type2 - 깍두기
# segmentation to 4, classificate the new customers.


# 1. Data and Libraries
import pandas as pd
train = pd.read_csv("/kaggle/input/big-data-analytics-certification-kr-2022/train.csv")
test = pd.read_csv("/kaggle/input/big-data-analytics-certification-kr-2022/test.csv")



# 2. EDA
# target 확인
# train['Segmentation'].value_counts()

# type 확인
# train.info()

# missing values 확인
# train.isnull().sum()
# test.isnull().sum()



# 3. Preprocessing
# target(y, label) 값 복사
target = train.pop('Segmentation')

# test데이터 ID 복사
test_ID = test.pop('ID')


# 수치형 컬럼
# ['ID', 'Age', 'Work_Experience', 'Family_Size', 'Segmentation']

# 사용할 컬럼들에 대해 확인 및 지정
num_cols = ['Age', 'Work_Experience', 'Family_Size']
train = train[num_cols]    # - train
# train.head(2)
test = test[num_cols]     # - test
# test.head(2)



# 4. Modeling
# 모델 선택 및 학습
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state = 2023)
rf.fit(train, target)
pred = rf.predict(test)
# pred     # 확인하기



# 5. Predict and to_csv
# 예측 결과를 데이터 프레임으로 만들기
# pd.DataFrame({'cust_id': X_test.cust_id, 'gender': pred}).to_csv('003000000.csv', index=False)
submit = pd.DataFrame({'ID': test_ID,'Segmentation': pred})
submit.to_csv('submission.csv', index = False)
