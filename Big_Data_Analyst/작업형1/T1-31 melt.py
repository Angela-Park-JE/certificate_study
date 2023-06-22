# 617 JungEun : 230615 THU mission 28 (1)
# T1-31. 데이터 재구성
# name 컬럼을 제외한 각 점수에 대해 모두 병합하여 가장 큰 5개 점수 더하여 출력.
# https://www.kaggle.com/code/angellapark/t1-31-melt

# 1. Data and libraries
import pandas as pd
df = pd.DataFrame({'Name': {0: '김딴짓', 1: '박분기', 2: '이퇴근'},
                   '수학': {0: 90, 1: 93, 2: 85},
                   '영어': {0: 92, 1: 84, 2: 86},
                   '국어': {0: 91, 1: 94, 2: 83},})



# 2. drop a meaningless column
df2 = df.drop(columns = 'Name').melt()


# 3. get value with sorting
print(df2['value'].sort_values(ascending = False)[:5].sum())



# --=
# 풀이
df = pd.melt(df, id_vars=['Name'])
df = df.sort_values(by='value', ascending=False)
print(sum(df['value'].iloc[:5]))


# 답 : 460
