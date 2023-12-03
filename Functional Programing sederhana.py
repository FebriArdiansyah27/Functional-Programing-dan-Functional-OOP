 def square(x):
    return x * x


def map(func, lst):
    return [func(x) for x in lst]


numbers = [1, 2, 3, 4, 5]

squares = map(square, numbers)
   
print(squares)
