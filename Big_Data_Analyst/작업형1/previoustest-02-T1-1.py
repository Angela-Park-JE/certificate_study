# 617 JungEun : 230608 THU mission 22 (1) 
# 2th type1-1
# 'f5' 기준 상위 10개 데이터 중 최소값으로 상위 10개 데이터를 대체하고
# 'age' 컬럼에서 80이상인 데이터에 대해 'f5' 컬럼 평균 구하기

# 1. Data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Get 10 data ordered by 'f5'
f5min = df['f5'].sort_values(ascending = False)[:10].min()
# 인덱스는 정수인덱스이므로
df.loc[:10, 'f5'] = f5min



# 3. the average of 'f5' in ('age' >= 80)
print(df[df['age']>=80]['f5'].mean())

# 62.76223596304349



# 풀이 
# 라이브러리 및 데이터 불러오기
import pandas as pd

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df.head()

# f5컬럼을 기준으로 내림차순 정렬
df = df.sort_values('f5', ascending=False)
df.head(10)

# 최소값 찾기
min = df['f5'][:10].min()
# min = 91.297791
min


df.iloc[:10,-1] = min
df.head(10)

# 80세 이상의 f5컬럼 평균
print(df[df['age']>=80]['f5'].mean())
