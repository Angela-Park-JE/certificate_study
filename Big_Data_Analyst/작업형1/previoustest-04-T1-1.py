# T1-1. age 컬럼의 3사분위수와 1사분위수의 차를 절대값으로 구하고, 소수점 버려서, 정수로 출력

# 617 JungEun : 230606 TUE mission 20 (1)
# 4th type1-1

import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")

diff = abs(df['age'].quantile(0.75) - df['age'].quantile(0.25))
print(int(diff))

# 50



# 풀이
import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
# print("1사분위: ",df['age'].quantile(0.25))
# print("3사분위: ",df['age'].quantile(0.75))

result = abs(df['age'].quantile(0.25) - df['age'].quantile(0.75))
# print("절대값 차이: ",result)

print(int(result))
