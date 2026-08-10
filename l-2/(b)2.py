arr=[20,50,70,40,30,10,60]

key = int(input("Enter the element to search [10-70]: "))

arr.sort()

print("Sorted array:", arr)

low = 0
high = len(arr) - 1
position = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        position = mid
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if position != -1:
    print("Element found at position", position + 1)
else:
    print("Element not found")