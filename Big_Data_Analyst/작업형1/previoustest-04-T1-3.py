# T1-3. date_added가 2018년 1월 이면서 country가 United Kingdom 단독 제작인 데이터의 갯수

# 617 JungEun : 230606 TUE mission 20 (1)
# 4th type1-3

import pandas as pd
df = pd.read_csv("/kaggle/input/big-data-analytics-certification-kr-2022/nf.csv")

df['date_ad1'] = pd.to_datetime(df['date_added'])
cond1 = df['country'] == "United Kingdom"
cond2 = df['date_ad1'].between('2018-01-01', '2018-01-31')

len(df[cond1&cond2])

# 6



# 풀이

# 풀이1 datatime 활용1
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")

cond1 = df['country'] == "United Kingdom"

df['date_added'] = pd.to_datetime(df['date_added'])
df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month


cond2 = df['year'] == 2018
cond3 = df['month'] == 1

print(len(df[cond1 & cond2 & cond3]))
# print(df[cond1 & cond2 & cond3])



# 풀이2 datatime 활용2 : >=, <= 사용
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")

cond1 = df['country'] == "United Kingdom"

df['date_added'] = pd.to_datetime(df['date_added'])

cond2 = df['date_added'] >= '2018-1-1'
cond3 = df['date_added'] <= '2018-1-31'

print(len(df[cond1 & cond2 & cond3]))



# 풀이3 datatime + between 활용 *** 베스트
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")

cond1 = df['country'] == "United Kingdom"
df['date_added'] = pd.to_datetime(df['date_added'])
cond2 = df['date_added'].between('2018-1-1', '2018-1-31')
print(len(df[cond1 & cond2]))



# 풀이4 문자로 날짜에 2018과 January 검색을 조건
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")

cond1 = df['country'] == "United Kingdom"

df['date_added'] = df['date_added'].fillna("")

str1 = "2018"
str2 = "January"
cond2 = df['date_added'].str.contains(str1)
cond3 = df['date_added'].str.contains(str2)

print(len(df[cond1 & cond2 & cond3]))



# ---
# (추가 문제) 4. 그런데 만약 'country'컬럼에 대소문자 함께 있고, 띄어쓰기가 있는 것도 있고 없는 것도 있다면?

import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")

# 띄어쓰기 제거
df['country'] = df['country'].str.replace(' ','')

# 소문자로 변경 - 아예 모두 변경해서 
df['country'] = df['country'].str.lower()
df['country']

# 붙여진 상태로 검색 (한 곳만 있는 곳은 '==' 으로 검색이 됨)
cond1 = df['country'] == "unitedkingdom"

df['date_added'] = pd.to_datetime(df['date_added'])
df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month


cond2 = df['year'] == 2018
cond3 = df['month'] == 1

print(len(df[cond1 & cond2 & cond3]))
