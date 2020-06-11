#to create a program that is divisible by 75 and 100
print("enter the ranges")
range1=int(input())
range2=int(input())
for i in range(range1,range2+1):
    if(i%75==0 and i%100==0):
         print(i)