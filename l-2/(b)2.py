arr = [20, 50, 70, 40, 30, 10, 60]

key = int(input("Enter element to search: "))

arr.sort()

print("Sorted array:", arr)

low = 0
high = len(arr) - 1
found = 0

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        found = 1
        break

    elif key < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == 0:
    print("Element not found")