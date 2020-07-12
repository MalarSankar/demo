f=lambda a:"True" if (round(a**(1/3))**3==a) else "False"
number=int(input("enter number:"))
print(f(number))
