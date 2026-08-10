e_id=[101,102,103,104,105,106,107]
s_id=int(input("Enter Employee ID from(101-107) to search:"))

def search_employee(e_id,s_id,i):
    if i==len(e_id):
        return False

    if e_id[i]==s_id:
        return True

    return search_employee(e_id, s_id, i + 1)


if search_employee(e_id, s_id, 0):
    print("Employee found.")
else:
    print("Employee not found.")