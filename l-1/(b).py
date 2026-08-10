p=int(input("Enter the principle growth factor value:"))
n=int(input("Enter the number of years:"))

def ci(p, n):
    if n>0:
        return p*ci(p, n-1)
    else:
        return 1

print("The compound interest is:", ci(p, n))