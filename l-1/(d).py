n=int(input("Enter a number of parcels: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("The number of ways the parcels can be arranged is",factorial(n))