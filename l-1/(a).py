def countdown(n):
    if n == 1:
        print(1)
        print("Launch!")
    else:
        print(n)
        countdown(n - 1)

n = int(input("Enter the countdown number: "))
countdown(n)
