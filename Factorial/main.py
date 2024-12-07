def factorial(x):
    '''this is a recursive function to find the factorial of a number'''

    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
    
x = int(input("Enter a number: "))
print(factorial(x))    