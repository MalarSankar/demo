f=open("filehandling.txt",'w')
f.write("hi i am Malar \n"
        "my d.o.b is 30/10/98")
f=open("filehandling.txt",'a')
f.write("\nI am a B.E degree holder")
f=open("filehandling.txt",'r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()


'''for data in f:
    print(data)'''
