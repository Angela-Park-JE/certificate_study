# 617 JungEun : 230620 TUE mission 32 (3)
# T1-3. 순전입 학생이 가장 많은 학교의 전체학생수 (순전입 학생 = 전입 학생 - 전출 학생) 
# '정수'로 출력

# 정답
# 1. 데이터, 라이브러리
import numpy as np
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0620 - 미션32/5-3student.csv')
# df.columns

# 2. new col 
df['순전입학생수(계)'] = df['전입학생수(계)'] - df['전출학생수(계)']

# 3. 정렬
df.sort_values('순전입학생수(계)', ascending = False)[:5]

# 4. 데려오기
temp = df.sort_values('순전입학생수(계)', ascending = False).reset_index()
answer = temp['전체학생수(계)'][0]
print(int(answer))



# 틀렸던 것
# 1. 데이터, 라이브러리
import numpy as np
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0620 - 미션32/5-3student.csv')
# df.columns

# 2. new col 
df['순전입학생수(계)'] = df['전입학생수(계)'] - df['전출학생수(계)']

# 3. find the school and get unique num
sc_code = df.sort_values('순전입학생수(계)', ascending = False)['정보공시 학교코드'][0] 
# 인덱스로 검색해서 인덱스상 첫번째 학교나옴 ㅎㅎ 
# 이렇게 하려면 리셋인덱스를 하던지 
# 아니면 데이터 프레임 말고 데이터 시리즈로만 가져와서 첫번째의 인덱스을 데려와서 그거로 인덱스 검색을 하던지 했어야 했음

# 4. print
print(int(df[df['정보공시 학교코드'] == sc_code]['전체학생수(계)']))

# 611
# 약 7~8분



# 복습 230913
# 3번 : 또 틀렸당
# 1. data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/mssion32-mission33-dataset/0620 - 미션32/5-3student.csv')

# 2. calculation
# 순전입학생이 가장 많은 학교의 전체학생수 (순전입 학생 = 전입 학생 - 전출 학생) 정수로
df['순전입학생'] = (df['전입학생수(계)'] - df['전출학생수(계)'])

# 3. condition
# answer = df.sort_values('순전입학생', ascending = False)['전체학생수(계)'][0]  # 틀림: 그대로 인덱스로 찾으면 원래 인덱스로 가져오게됨.
data = df.sort_values('순전입학생', ascending = False)['전체학생수(계)'].reset_index(drop = True)
answer = int(data[0])

print(answer)
