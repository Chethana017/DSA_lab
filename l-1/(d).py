def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number of parcels: "))

if n < 0:
    print(f"The factorial of {n} is not defined")
else:
    print("Number of possible arrangements of parcels:", factorial(n))