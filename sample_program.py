#program for break operator
list=[1,2,3,4,5]
for i in list:
    if i==3:
        break
    print(i)

#program for  continue operator
for i in range(5):
    if i==3:
        continue
    print(i)

#program for pass operator
list1=[1,2,3,4,5]
for i in list1:
    if i==3:
        pass
        print("nothing to execute")
    print(i)
