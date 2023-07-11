# 617 JungEun : 230607 WED mission 21 (1)
# 3th type1-3
# 결측치가 제일 큰 값의 컬럼명을 구하시오

# 1. Data and libraries
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")


# 2. count missing values
mv = df.isna().sum()
# sorting by 'null' counts
mv.sort_values(ascending = False, inplace = True)


# 3. print the index of 1st row
print(mv.index[0])

# f1



# solution

# 풀이1
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")

df = pd.DataFrame(df.isnull().sum(), columns=['cnt_null'])
df = df['cnt_null'].sort_values(ascending=False)
print(df.index[0])


# 풀이2
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")

df = df.isnull().sum()
print(df.index[3])
