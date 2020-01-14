"""
first_name = "kim"
last_name = "taewoo"

full_name = first_name + " "+last_name
print(full_name)

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

print("{}*{}={}".format(3, 4, 3*4))


txt = "python"
print(txt[0:2])
print(txt[1:4])
print(txt[-3:-1])

txt = "Hi, Kim!"
txts = txt.split(",")
print(type(txts))
print(txts)
"""
"""


age = 15
if age <8:
    print("이용료는 5000")
elif age>=8 and age < 20:
    print("이용로는 15000")
elif age>=20 and age < 60:
    print("이용로는 20000")
else:
    print("이용못함")

"""
"""
players = ['tw', 'yj', 'hd', 'hs']
print(players)
for player in players[:2]:
    print(player)

players[0] = 'ducayi'
players[1:3] = ['holly', 'bmw']
print(players)

players.append('ohd')
print(players)
"""

"""

items = ("ruler", "pen", "eraser")
item1, item2, item3 = items
print(item1)
print(item2)
print(item3)

num1 = 3
num2 = 5
num1, num2 = num2, num1
print(num1)
print(num2)
"""
"""
alien={'color':'green', 'point':5}
print(alien)

del alien['point']
print(alien)

c=alien.pop('color')
print(c)
print(alien)
"""
"""
content_ratings = {'4+':4433, '9+':987, '12+':1155, '17+':622}
print(content_ratings)

over_9 = content_ratings['9+']
over_17 = content_ratings['17+']
print(over_9)
print(over_17)

content_ratings = {}
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622
print(content_ratings['12+'])
"""

"""
apps_of_ages = {'4+':4433, '9+':987, '12+':1155, '17+':622}
total_apps = 7197
ratios = {}
percentages = {}
for apps_of_age in apps_of_ages:
    ratios[apps_of_age] = apps_of_ages[apps_of_age] / total_apps
    percentages[apps_of_age] =ratios[apps_of_age] * 100

print(ratios)
print(percentages)
"""

"""
def describe_pet(name, type='dog'): #이런식으로 디폴트 값을 줄 수도 있음
    print("\nI have a "+ type + ".")
    print("My " + type + "'s name is "+ name.title() + ".")

describe_pet(type='hamster', name = 'harry') #이렇게 키워드를 이용한 파라미터 전달도 가능
describe_pet('tw')
describe_pet('yj', 'skung')
"""

"""

def grade(*scores):
    score_sum = 0
    for score in scores:
        score_sum += score
    score_avg = score_sum / len(scores)

    if score_avg >= 90:
        grade = 'A'
    elif score_avg>=80:
        grade = 'B'
    elif score_avg>=70:
        grade = 'C'
    else:
        grade = 'F'

    return grade

print(grade(84,69,75))
"""

"""


from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}
page = requests.get('https://www.google.com', headers=header)
print(page.content)
"""

"""
url = "https://www.naver.com/"
response = requests.get(url)
print(response)

data = response.text
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('a')
print(tags)
"""

"""
from bs4 import BeautifulSoup

def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data

html_file = read_file('tw.html')
soup = BeautifulSoup(html_file, 'lxml')
print(soup.prettify())
"""


#원하는 태그 추출
"""
from bs4 import BeautifulSoup

def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file('tw.html'), 'lxml')
meta = soup.meta
print(meta)
print(meta.name)
print(meta.get('charset'))

body = soup.body
print(body.div)
"""

"""
import warnings
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file('tw2.html'), 'lxml')
body = soup.body
print(type(body.children))

for child in body.children:
    print(child if child is not None else ", end='\n\n\n\n'")
"""

"""
from bs4 import BeautifulSoup
def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file('tw3.html'), 'lxml')
a_tags = soup.find_all('a')
print(a_tags)

attr = {'class':'sister', 'id':'link1'}
first_a = soup.find_all('a', attrs = attr)
print(first_a)
"""

"""
from bs4 import BeautifulSoup
import re

def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file('tw3.html'), 'lxml')
regex = re.compile('Elsie')
tags = soup.find_all(string = regex)
print(tags)
"""

#실시간 검색기
"""
from bs4 import BeautifulSoup
import requests

url = "https://datalab.naver.com/"
response = requests.get(url)
print(response)

data = response.text
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('span')

tags2 = soup.find_all('span', {'class' : 'title'})
for t in tags2:
    print(t)
#print(tags)
print(tags2)
"""

#크롤러
"""
from bs4 import BeautifulSoup
import requests
import re

url = "https://www.consumerreports.org/cro/a-to-z-index/products/index.htm"
response = requests.get(url)
print(response)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

tag = soup.find_all('a', {'class' : 'products-a-z__results__item'})

for string in tag:
    string = str(string)
    string = re.match('<.*?>', string).group()
    string = string.replace(string[:44], "")
    string = string.replace(string[-1], "")
    print(string)

for tag in soup.select('a[class=products-a-z__results__item]'):
    print(tag.text)

"""
#크롤러2
from bs4 import BeautifulSoup
import requests
import re

url_list=[]
url = "https://codingbat.com/java/Warmup-1"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

tag = soup.find_all('a')
for string in tag:
    string = str(string)
    string = re.match('<.*?>', string).group()
    string = string[10:]
    string = string.replace(string[-1], "")
    string = string.replace(string[-1], "")
    if('prob' == string[:4]):
        url_list.append(string)

print(url_list)
for s in url_list:
    url = "https://codingbat.com/" + s
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    tag = soup.find_all('p', {'class': 'max2'})

    for s in tag:
        print(s.string)
