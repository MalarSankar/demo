string1=str(input("enter string1:"))
string2=str(input("enter string2:"))
if(string1.isalpha() and string2.isalpha()):
    if(sorted(string1.lower())==sorted(string2.lower())):
        print("True")
    else:
        print("False")
else:
    print("give a valid string")