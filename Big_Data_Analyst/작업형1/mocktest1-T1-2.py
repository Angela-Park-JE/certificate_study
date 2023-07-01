# 617 JungEun : 230612 MON mission 25 (2)
# 모의고사 T1-2
# 'f4' descending 'f5' ascending 정렬 후, 앞에서부터 10개 데이터 중 'f5' 컬럼의 최소값을 찾음
# 이 최소값으로 앞 'f5' 10개 데이터를 변경한 뒤 'f5'의 평균을 구하라. 셋째 자리에서 반올림하여 둘째 자리까지 출력

# 1. Data and libraries
import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")


# 2. Ordering and minimum value in 10th values of ordered data
df = df.sort_values(['f4', 'f5'], ascending = [False, True])
df.iloc[:10, 7] = df[:10]['f5'].min() 


# 3. average of 'f5' column 
print(round(df['f5'].mean(), 2))
