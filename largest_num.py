number=int(input("enter number:"))
list1=list(map(int,str(number)))
list1=sorted(list1)
res=list1[::-1]
for i in res:
    print(i,end="")