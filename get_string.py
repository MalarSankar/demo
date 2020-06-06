#program to get a string in list
list1=["abc",[2,3,("xyz","the avengers")],1,2,3]
#extract nested list2 from list1
list2=list1[1]
#print(list2)
#change list2 into tuple
tuple1=tuple(list2)
#print(tuple1)
#now print the exact value
print(tuple1[2][1][4:11])



