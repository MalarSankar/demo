#to create a function for find country name
def get_country(val):
    for key,value in dict.items():
        if val==value:
            print(key)
#to create a empty dictionary
dict={}
n=int(input("enter the number of elements in dictionary:"))
for i in range (n):
    key=input("enter key:")
    value=input("enter value")
    dict.update({key:value})
print("the dictionary is",dict)
# to call the function
desired_continent=input("enter the desired continent")
if(desired_continent[0].islower()):
    get_country(desired_continent)
else:
    str=desired_continent[0].lower()+desired_continent[1:]
    get_country((str))