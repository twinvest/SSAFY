import pandas as pd

data = ['2016','2017','2018','2019']
result = pd.Series(data)
print(result)
print()
print(result.index)
print()
print(result.values)
print()

result.name='Year'
result.index.name = 'No'
print(result)
print()

data = ['2016','2017','2018','2019']
result = pd.Series(data, index =['a','b','c','d'])
print(result)
print()
print(result.index)
print()

score = {'Kim':85, 'Hwang':100, 'Lee':99, 'Choi':80}
result = pd.Series(score)
print(result)
print()
print(result.index)
print()
print(result.values)
print()
print(result['Lee'])
print()
print(result['Hwang'])

data = {'name' : ['Lee', 'Hwang', 'Kim', 'Choi'],
        'score' : [100,95,90,85],
        'greade' : ['A','B','C','D']}
df = pd.DataFrame(data)
print(df)
print()
print(df.index)
print()
print(df.columns)
print()
print(df.values)
print()

df.index.name = 'No'
df.columns.name = 'Info'
print(df)
print()

c=['name', 'grade', 'score', 'etc'] #etc컬럼을 추가하면
df2 = pd.DataFrame(data, columns=c) #etc컬럼을 추가하면
print(df2) #자동으로 nan으로 초기화됨.
print()

score = {'Kim':85, 'Hwang':100, 'Lee':99, 'Choi':80}
students = ['Hwang','Lee','Woo']
result = pd. Series(score, index=students)
print(result)
print()

"""
#연습문제
#1번 데이터프레임 객체 생성하기
data = {'name' : ['David', 'Roy', 'Tina', 'Kim'],
        'score' : [78,64,70,62],
        'grade' : ['C','D','C','D']}
df = pd.DataFrame(data)
df.index.name = 'No'
df.columns.name = 'Info'
print(df)
print()

c=['name', 'grade', 'score', 'etc']
df2 = pd.DataFrame(data, columns=c) #etc컬럼을 추가하면
print(df2) #자동으로 nan으로 초기화됨.
print()

#2번 인덱스, 컬럼, 데이터값 조회
print(df2.index)
print()
print(df2.values)
print()
"""
print(df2['name'])
print()
print(df2.name)
print()
print(df2[['name','grade']])
print()
print(df2[['etc','name']])
print()
df2['etc'] = 0
print(df2)
print()

#연습문제3
df2['grade'] = ['A','B','C','D']
df2['etc'] = [11, 22, 33, 44]
print(df2)
print()