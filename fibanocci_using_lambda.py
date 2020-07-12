#reduce function
from functools import reduce
fib=lambda max_range:reduce(lambda x,_:x+[x[-1]+x[-2]],range(max_range-2),[0,1])
max_range=int(input("enter maximum range:"))
print(fib(max_range))
