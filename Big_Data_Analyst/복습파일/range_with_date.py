# date로 range를 만드는 방식
# 날짜 형식의 데이터 값을 준 뒤, 범위를 date 기준으로 정한다.
# 20230509로 시작하여 7일간의 index를 만드는 방식
import pandas as pd
s = pd.Series([1,2,3,4,5,6,7], index = pd.date_range("20230509", periods = 7))

# 따라서 날짜로 인덱스를 불러오게 되면 다음과 같이 쓸 수 있다.
s['20230510':'20230512'].sum()
