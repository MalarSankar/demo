#to extract domain name in url
import tldextract
url='https://www.hackerrank.com/domains/python'
domain_name=tldextract.extract(url)
print(domain_name.registered_domain)