import pandas as pd
import numpy as np

data = {'name' : ['Lee', 'Hwang', 'Kim', 'Choi'],
        'score' : [100,95,90,85],
        'greade' : ['A','B','C','D']}
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