import re
string = '<a class="products-a-z__results__item" href="/cro/air-filters.htm"> vAir Filters </a>'
print(re.match('<.*?>', string).group())


"""
regex = re.match('<.*?>', string)
p = regex.search(str)
print(type(p))
print(type(p))
"""