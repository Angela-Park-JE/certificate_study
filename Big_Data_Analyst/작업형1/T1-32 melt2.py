# 617 JungEun : 230616 FRI mission 29 (1)
# T1-31. 데이터 재구성
# name 컬럼을 제외한 각 점수에 대해 모두 병합하여 가장 큰 5개 점수 더하여 출력.

# 1. Data and libraries
import pandas as pd
df = pd.DataFrame({'Name': {0: '김딴짓', 1: '박분기', 2: '이퇴근'},
                   '수학': {0: 90, 1: 93, 2: 85},
                   '영어': {0: 92, 1: 84, 2: 86},
                   '국어': {0: 91, 1: 94, 2: 83},})


# 2. unpivot the data about col '수학', '영어'
df2 = df.melt(id_vars = 'Name', value_vars = ['수학', '영어'])


# 3. get average to intager, about >=90 data
print(int(df2[df2['value']>=90]['value'].mean()))



# ---
# 풀이
df = pd.melt(df, id_vars=['Name'], value_vars=['수학', '영어'])
cond = df['value'] >= 90
print(int(df[cond]['value'].mean()))

# 답 : 91
