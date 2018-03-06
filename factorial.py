def factorial(x):
    product = 1
    while x>=1:
        product = product * x
        x = x-1
    return product

print (factorial(5))
#print(range(3))