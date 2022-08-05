def superFunc(name, *args, i='hi', **kwargs):
    return sum(args) + sum(kwargs.values())


print(superFunc('Omar', 1, 2, 3, 4, 5, num1=10, num2=20))

# rule: parameters, *args, default parameters, **kwargs
# *args: used to pass a list of arguments
# **kwargs: used to pass a dictionary of arguments
# default parameters: used to set a default value for a parameter
# parameters: used to define the type of data that a function accepts
