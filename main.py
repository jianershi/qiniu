from qiniulib import *
from credentials import baseUrl

items = list_all('sekai')
for item in items:
		url=baseUrl+item['key']
		part = url.split()
		print part[0]+'%20'+part[1]