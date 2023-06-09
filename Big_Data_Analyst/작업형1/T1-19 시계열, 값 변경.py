# 617 JungEun : 230601 THU mission 16 (2)
# T1-19. 시계열 데이터, 날짜, 그룹화, 조건에 따라 값 변경
# 2022, 2023 연별로 월별 총 Sales의 맥스값을 비교하기

# 1. Data and libraries
import pandas as pd
df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic2.csv')



# 2. Sales value reflecting 'Events' columns : if 'events' = 1 than 'sales'*0.8
# 해당 조건에 맞게 새 컬럼에 수정된 값을 넣습니다.
df['Sales_adm'] = df[df['Events'] == 1]['Sales']*0.8
# 그리고 조건에 맞지 않는 행은 결측치로 처리되기 때문에 fillna로 기존 세일즈 값을 넣습니다.
df['Sales_adm'].fillna(df['Sales'], inplace = True)



# 3. Devide dataset to 2022 set and 2023 set
df['Date'] = pd.to_datetime(df['Date'])
df2022 = df[df['Date'].dt.year == 2022]
df2023 = df[df['Date'].dt.year == 2023]



# 4. Get Monthly total 'Sales' 
# This data has data with just 2022 and 2023, so I just made by monthly directly
montlysales22 = df2022.groupby(df2022['Date'].dt.month)['Sales_adm'].sum()
montlysales23 = df2023.groupby(df2023['Date'].dt.month)['Sales_adm'].sum()



# 5. Calculate Max monthly sales' diff
max22, max23 = montlysales22.max(), montlysales23.max()
print(int(round(abs(max22-max23))))
