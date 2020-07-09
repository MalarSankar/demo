import re
url=input("enter the url")
m=re.search('https?://([a-z0-9.]+).*',url)
print(m.group(1))
