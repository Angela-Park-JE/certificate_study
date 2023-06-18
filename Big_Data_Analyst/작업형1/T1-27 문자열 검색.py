# 617 JungEun : 230610 SAT mission 24 (2)
# T1-27 바닐라라떼 5, 카페라떼 3, 아메리카노 2, 나머지 0.
# 총 메뉴의 점수를 더한 값

### 23.06.10 :
# 16~17분 걸림. 무식하게 값을 다 데이터프레임에 때려박을 생각만 함. 조건에 맞는 세 가지 메뉴의 로우만 개수 세서 곱하기로 점수 내면 되는데.

# 1. Data and libraries
import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/payment.csv")
# df



# 2. preprocessing : str를 안껴주면 안바뀐다.
df['menu'] = df['menu'].str.replace(' ', '')



# 3. making new column : 딕셔너리로 람다를 이용해 채워넣으려 했으나 실패
# point = {'바닐라라떼':5, '카페라떼':3, '아메리카노':2}
# 그래서 일일히 넣었다고. : # df[df['menu'] == '아메리카노']['points'] = 2 -> 이방식은 안됨. 카피셋팅오류나니 loc를 사용하라며 값이 안들어감.
df['points'] = 0
df.loc[df[df['menu'] == '바닐라라떼'].index, 'points'] = 5
df.loc[df[df['menu'] == '카페라떼'].index, 'points'] = 3
df.loc[df[df['menu'] == '아메리카노'].index, 'points'] = 2



# 4. Sum all points
print(sum(df['points']))   # 17




# ---
# 풀이
df['menu'] = df['menu'].str.replace(' ','')

s1 = sum(df['menu'].str.contains("바닐라라떼"))
s2 = sum(df['menu'].str.contains("카페라떼"))
s3 = sum(df['menu'].str.contains("아메리카노"))
print((s1*5) + (s2*3) + (s3*2))

# 답 : 17
