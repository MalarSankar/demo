def function_outside():
    msg="Hi"
    def function_inside():
        msg="Hello"
        print(msg)
    return function_inside
a=function_outside()
a()
a()

def f(x):
    def g(y):
        return y
    return g
a=5
b=1
h=f(a)
print(h(b))
'''I have return the reference of inner function(i.e g). return g refers only the inner function so i pass argument 1 to
that function  and that inner function return 1 '''
