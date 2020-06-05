#create a dictionary input from user
dict={}
n=int(input("enter the number of elements in dictionary:"))
for i in range (n):
    key=input("enter key:")
    value=input("enter value")
    dict.update({key:value})
print("the dictionary is",dict)
# find a key in dictionary
search_key=input("enter search key")
if search_key in dict.keys():
    print("key is exist")
else:
    print("key is not exist")