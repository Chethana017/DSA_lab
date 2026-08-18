arr = [10, 20, 30, 40, 50]

key = int(input("Enter element to search[10-50]: "))

found = 0

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = 1
        break

if found == 0:
    print("Element not found")