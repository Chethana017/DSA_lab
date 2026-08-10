n=int(input("Enter a number to start the countdown: "))
print("The rocket will launch in.....")

def countdown(n):
    if n == 0:
        print("launch!")
    else:
        print(n)
        countdown(n - 1)

countdown(n)