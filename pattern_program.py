#to create a pattern program
import math
def pattern(n):
    div=math.ceil((n/2))
    div1=n-div
    k=1
    for i in range(div):
        for j in range(0,k):
                print("*",end=" ")
        k=k+2
        print()
    l=n-2
    for i in range(div1):
        for j in range(0,l):
            print("*",end=" ")
        l=l-2
        print()
print("enter the rows")
n=int(input())
pattern(n)