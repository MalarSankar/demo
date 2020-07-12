def exception():
    try:
        num=int(input("enter input:"))
    except Exception as e:
        print("enter the input as an integer,",e)
        exception()

exception()
print("entered an integer")
