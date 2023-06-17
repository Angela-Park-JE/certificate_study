# 617 JungEun : 230609 FRI mission 23 (4) 
# T1-26 STR contains
# payment 데이터에서 menu컬럼에 "라떼" 키워드가 있는 데이터의 수

# 1. Data and Libraries
import pandas as pd
df = pd.read_csv("/kaggle/input/bigdatacertificationkr/payment.csv")



# 2. 방법1 : text.find() 쓰기
df['라떼를찾아라'] = df['menu'].str.find('라떼')
cnts = len(df[df['라떼를찾아라'] != -1])
# print(cnts)



# 3. 방법2 : 풀이에서 쓴 text.contains() 쓰기 : 출처 [https://ponyozzang.tistory.com/622]
# 결측치가 있을 경우 어떻게 처리할지 정해주어야 에러가 나지 않는다.
# NaN이 존재하는 경우 False로 치환 : # print(df['name'].str.contains('li', na = False))
cnts2 = df['menu'].str.contains('라떼', na = False).sum()
print(cnts2)





# ---
# 풀이
print(sum(df['menu'].str.contains("라떼")))


# 답 : 10
