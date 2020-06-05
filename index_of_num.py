#to find index of a number
list1=[1,2,4,5,1,1,4,1,56]
list2=[i for i in range(len(list1))
       if list1[i]==1]
print(list2)