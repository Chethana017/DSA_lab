n=int(input("Enter a number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    print("The number of ways the parcels can be arranged is",factorial(n))