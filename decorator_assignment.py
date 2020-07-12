def outer_fun(func):
    def inner_fun():
        return "outer "+func()+"outer "
    return inner_fun
def outer1_fun(func):
    def inner1_fun():
        return "inner "+func()+"inner "
    return inner1_fun
@outer_fun
@outer1_fun
def string():
    return "inside "
print(string())