def generator_function(n):
    for i in range(n):
        yield i


g = generator_function(100)
print(next(g))
print(next(g))
