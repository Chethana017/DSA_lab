class single_linked_list:
    #creating a node
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
    
    #creating a node
    def create(self):
        n = int(input("Enter number of elements:"))
        for i in range(n):
            x = int(input("Enter value:"))
            new = self.Node(x)
            if self.head is None:
                self.head = new
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new

    #insertion in sll-at the beginning
    def insert_beginning(self, data):
        new = self.Node(data)
        new.next = self.head
        self.head = new

    #insertion in sll-at the end
    def insert_end(self, data):
        new = self.Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    #insertion in sll-at a given position
    def insert_index(self, index, data):
        if index == 0:
            self.insert_beginning(data)
            return
        elif index > self.count():
            print("Invalid Index")
            return
        new = self.Node(data)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        new.next = temp.next

    #deletion in sll-at the beginning
    def delete_beginning(self):
        if self.head is None:
            print("No elements to delete")
        else:
            temp = self.head
            self.head = temp.next
            print("Deleted element = ", temp.data)
    
    #deletion in sll-at the end
    def delete_end(self):
        if self.head is None:
            print("No elements to delete")
            return
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            temp1=temp
            while temp.next:
                temp1 = temp
                temp = temp.next
            temp1.next = None
    
    #deletion in sll-at a given position
    def delete_index(self, index):
        if self.head is None:
            print("No elements to delete")
        else:
            temp = self.head
            if temp and temp.data == index:
                self.head = temp.next
                print("Value deleted")
                return
            while temp.next and temp.next.data != index:
                temp = temp.next
            if temp.next is None:
                print("Value not present")
            else:
                temp.next = temp.next.next
                print("Value deleted")

    #displaying the elements of sll
    def display(self):
        if self.head is None:
            print("No elements to display")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    #counting the number of elements in sll
    def count(self):
        if self.head is None:
            print("No elements to count")
        else:
            c = 0
            temp = self.head
            while temp:
                c += 1
                temp = temp.next
            return c

sll = single_linked_list()
while True:
    print("1. Create a single linked list")
    print("2. Insert at the beginning")
    print("3. Insert at the end")
    print("4. Insert at a given position")
    print("5. Delete at the beginning")
    print("6. Delete at the end")
    print("7. Delete at a given position")
    print("8. Display the list")
    print("9. Count the elements")
    print("10. Exit")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        sll.create()
    elif choice == 2:
        data = int(input("Enter value to insert:"))
        sll.insert_beginning(data)
    elif choice == 3:
        X = int(input("Enter value to insert:"))
        sll.insert_end(X)
    elif choice == 4:
        X = int(input("Enter value to insert:"))
        index = int(input("Enter index to insert:"))
        sll.insert_index(index, X)
    elif choice == 5:
        sll.delete_beginning()
    elif choice == 6:
        sll.delete_end()
    elif choice == 7:
        index = int(input("Enter value to delete:"))
        sll.delete_index(index)
    elif choice == 8:
        sll.display()
    elif choice == 9:
        count = sll.count()
        print("Number of nodes = ", count)
    elif choice == 10:
        break
    else:
        print("Invalid choice")