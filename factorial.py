def factorial(x):
    if x == 0 or x == 1:
        return x
    else:
        return  x*factorial(x-1)
print(factorial(5))