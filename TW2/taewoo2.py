import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

data = {'name' : ['Lee', 'Hwang', 'Kim', 'Choi'],
        'score' : [100,95,90,85],
        'grade' : ['A','B','C','D']}
df2 = pd.DataFrame(data)
df2['etc'] = np.zeros(4)
print(df2)
print()

points = pd.Series([1.5,1.7,2.4], index=[0,1,2])
print(points)
print()

df2['points'] = points
print(df2)
print()

df2['high_score'] = df2['score'] > 90
print(df2)
print()

df2.loc[4,:] = ['C', 'Su', 50, 0.0, 1.1, False]
print(df2)
print()

del df2['etc'] #열을 삭제
print(df2)
print()

df2.drop(4) #행을 삭제. 하지만 이는 기존 원본객체를 건드리지 않음
df2.drop(4, inplace=True) #행을 원본객체에서 삭제
print(df2)
print()

df2.set_index('name', inplace=True)
print(df2)
print()

print(df2[1:3])
print()
print(df2[:2])
print()

print(df2.loc['Lee'])
print()
print(df2.loc[['Lee','Choi']])
print()

print(df2.loc[:'Kim'])
print()

print(df2.loc['Kim':'Choi', ['grade', 'high_score']])
print()

print(df2.iloc[0:3])
print()
print(df2.iloc[0:3, 1:3]) #iloc[행 조건식, 열 조건식] ==>열 조건식은 생략할수도 있음
print()

print(df2.loc[df2['points']>1.5, :])
print()
print(df2.loc[df2['grade']=='A', :])
print()

df = pd.DataFrame(np.arange(18).reshape(6,3), index=['a','b','c','d','e','f'], columns=['x','y','z'])
df['data1'] = pd.Series([1.7,1.2,2.4], index=['a','e','c'])
print(df)
print()
df['date'] = pd.date_range('20190717', periods=6)
print(df)
print()

#원본 객체는 변경되지 않음
df2 = df.dropna(how='any')
print(df2)
print(df)
print()

#NaN추가
df['data2'] = np.nan
print(df)
print()

df = df.fillna(value='not null') #마찬가지로 원본데이터는 변경되지 않음. 원본데이터를 변경하고 싶으면 inplace=True를 추가해주면 된다.
print(df)
print()
