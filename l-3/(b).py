n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = key
print("Sorted list:", arr)
