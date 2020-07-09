import re
number=input("enter number:")
if(re.search("[-+]?[0-9]*\.[0-9]*",number)):
    print("True")
else:
    print("False")