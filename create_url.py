#to create url program
from urllib.parse import *
url=urlparse('www.hackerrank.com/domains/python')
print(url)
unparse_url=urlunparse(url)
print(unparse_url)
#another method to create url
url=urlunparse(('https','www','hackerrank','com','domains','python'))
print(url)

