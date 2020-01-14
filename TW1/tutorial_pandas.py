import pandas as pd

data = ['2016', '2017', '2018', '2019']
result = pd.Series(data)

#print(result)
#print(result.index)
#print(result.values)
"""
result.name = 'Year'
result.index.name = 'No'
print(result)
"""

"""
result = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(result)
"""

def pandas_test():
    score = {'Kim': 85, 'Hwang': 100, 'Lee': 99, 'Choi': 80}
    result = pd.Series(score)
    return result

result = pandas_test()
print(result['Lee'])