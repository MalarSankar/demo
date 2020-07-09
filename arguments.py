def grade(name,*args):
    c=0
    for i  in args:
        c=c+i
    avg=c/len(args)
    print(name,"-",avg)
grade("ram",80,96,84,70,56)

