e_id=[101,102,103,104,105,106,107]
s_id=int(input("Enter Employee ID from(101-107) to search:"))

def search_employee(e_id,s_id,i):
    if i==len(e_id):
        return -1

    if e_id[i]==s_id:
        return i

    return search_employee(e_id, s_id, i + 1)

result=search_employee(e_id,s_id, 0)
if result != -1:
    print("Employee ID found at position:", result)
else:
    print("Employee not found.")