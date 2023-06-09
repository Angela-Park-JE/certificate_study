# 617 JungEun : 230603 SAT mission 18 (2)
# T1-23. 결측치 핸들링, 중복 제거, 중앙값
# 'f1' 컬럼에서 10번째로 큰 값으로 'f1'컬럼의 결측치를 대체한 뒤,
#  'age' 컬럼에서 중복제거, 제거 시 먼저 나온 것을 남기고, 
# 최종적으로는 중복을 지운 것과 지우지 않은 것의 'age' 중앙값 차이를 절댓값으로 구하기

# 1. Data and libraries
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')



# 2. Fill the missing values with 10th big value in 'f1'
# 이렇게 순서대로 해도 되고
# f1 = df['f1'].sort_values(ascending = False)[:10] # (시리즈 형태로 반환됨)
# f1_filler = f1.values[-1]
# 이렇게 한번에 넣어도 됩니다.
f1_filler = df['f1'].sort_values(ascending = False)[:10].values[-1]

df['f1'].fillna(f1_filler, inplace = True)



# 3. Make a new DataFrame dropped the duplicated data in the 'age' column
df_before = df.copy()
df_after = df.drop_duplicates(subset = ['age'], keep = 'first')



# 4. Median values of 'f1' in two datasets, before and after.
print(abs(df_before['f1'].median() - df_after['f1'].median()))



# -- 참고 --
# 만약 'f1' 기준 내림차순으로 전체 데이터 프레임을 수정했다면 중복제거 결과가 달라지기 때문에
# 결과적으로 중앙값 얻은 것도 달라집니다. (결과값: 8.5)
df_temp = df.sort_values(by = 'f1', ascending = False)
df_temp_before = df_temp.copy()
df_temp_after = df_temp.drop_duplicates(subset = ['age'], keep = 'first')
print(abs(df_temp_before['f1'].median() - df_temp_after['f1'].median()))



# ---
# 풀이
import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
# df.tail()

# f1데이터에서 10번째 큰 값으로 결측치를 채움
top10 = df['f1'].sort_values(ascending=False).iloc[9]
print(top10)
df['f1'] = df['f1'].fillna(top10)

# 중복 제거 전 중앙 값
result1 = df['f1'].median()
# result1

# 중복 제거
# print(df.shape)
df = df.drop_duplicates(subset=['age'])
# print(df.shape)

# 중복 제거 후 중앙 값
result2 = df['f1'].median()
# result2

# 차이 (절대값)
print(abs(result1 - result2))

# 답 : 0.5
