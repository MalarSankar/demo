import re
pan_num=input("enter pan number")
if(re.match("[A-Z]{5}[0-9]{4}[A-Z]{1}",pan_num)):
    print("True")
else:
    print("False")