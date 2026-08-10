arr = [10, 20, 30, 40, 50]

key = int(input("Enter the element to search [10-50]: "))

position = -1

for i in range(len(arr)):
    if arr[i] == key:
        position = i
        break

if position != -1:
    print("Element found at position", position + 1)
else:
    print("Element not found")