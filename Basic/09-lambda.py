# `function_name` = lambda `argument` : `return`
function = lambda a : a+5
print(function(10))         # 15

# advance (closure)
def myfunc(n):
    return lambda a : a*n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(10))        # 20
print(mytripler(10))        # 30
