#to create a function for find key
def get_country(val):
    for key,value in dict.items():
        if val==value:
            print(key)
        else:
            print("continent is not there")
#to create a empty dictionary
dict={}
n=int(input("enter the number of elements in dictionary:"))
for i in range (n):
    key=input("enter key:")
    value=input("enter value")
    dict.update({key:value})
print("the dictionary is",dict)

desired_continent=input("enter the desired continent")
get_country(desired_continent)