# 617 JungEun : 230605 MON mission 19 (1)
# 공식 예시문제 유형 1

# 데이터 파일 읽기 예제
import pandas as pd
df = pd.read_csv('data/mtcars.csv', index_col=0)


# 1. 'qsec' MinMax scaling
import sklearn.preprocessing

# dir 할 때에는 print를 써주어야 출력된다.
# print(dir(sklearn.preprocessing))
# sklearn.preprocessing.MinMaxScaler
mmscaler = sklearn.preprocessing.minmax_scale
df['qsec_scaled'] = mmscaler(df[['qsec']])



# 2. print the count of records
print(sum(df['qsec_scaled']>0.5))


# 9
