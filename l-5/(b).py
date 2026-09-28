class double_linked_list:
    #creating a node
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
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
                new.prev = temp
    
    #insertion in dll-at the beginning
    def insert_beginning(self, data):
        new = self.Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        print("Node inserted at the beginning.")

    #insertion in dll-at the end
    def insert_end(self, data):
        new = self.Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp
        print("Node inserted at the end.")
    
    #insertion in dll-at a given position
    def insert_index(self, index, data):
        if index < 0:
            print("Invalid Index")
        elif index == 0:
            self.insert_beginning(data)
        else:
            new = self.Node(data)
            temp = self.head
            for i in range(index - 1):
                if temp is None:
                    print("Invalid Index")
                    return
                temp = temp.next
            new.next = temp.next
            new.prev = temp
            if temp.next:
                temp.next.prev = new
            temp.next = new
        print("Node inserted at index", index)

    #deletion in dll-at the beginning
    def delete_beginning(self):
        if self.head is None:
            print("No elements to delete")
        elif self.head.next is None:
            self.head = None
            print("Deleted the only element in the list.")
        else:
            self.head.next.prev = None
            self.head = self.head.next
            print("Deleted element at the beginning.")

    #deletion in dll-at the end
    def delete_end(self):
        if self.head is None:
            print("No elements to delete")
        elif self.head.next is None:
            self.head = None
            print("Deleted the only element in the list.")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            temp.next = None
            print("Deleted element at the end.")
        
    #deletion in dll-at a given position
    def delete_index(self, index):
        if self.head is None:
            print("No elements to delete")
        elif index < 0:
            print("Invalid Index")  
        elif index == 0:
            self.delete_beginning() 
        else:
            temp = self.head
            for i in range(index):
                if temp is None:
                    print("Invalid Index")
                    return
                temp = temp.next
            if temp is None:
                print("Invalid Index")
            elif temp.next:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
            else:
                temp.prev.next = None
                temp.next = None
            print("Deleted element at index", index)

    #displaying the elements of dll in forward direction
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
    
    #displaying the elements of dll in backward direction
    def display_backward(self):
        temp = self.head
        if temp is None:
            print("None")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")
    
dll = double_linked_list()
while True:
    print("1. Create a new list")
    print("2. Insert at the beginning")
    print("3. Insert at the end")
    print("4. Insert at a given index")
    print("5. Delete from the beginning")
    print("6. Delete from the end")
    print("7. Delete from a given index")
    print("8. Display forward")
    print("9. Display backward")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        dll.create()
    elif choice == 2:
        data = int(input("Enter value to insert:"))
        dll.insert_beginning(data)
    elif choice == 3:
        data = int(input("Enter value to insert:"))
        dll.insert_end(data)
    elif choice == 4:
        index = int(input("Enter index to insert:"))
        data = int(input("Enter value to insert:"))
        dll.insert_index(index, data)
    elif choice == 5:
        dll.delete_beginning()
    elif choice == 6:
        dll.delete_end()
    elif choice == 7:
        index = int(input("Enter index to delete:"))
        dll.delete_index(index)
    elif choice == 8:
        dll.display_forward()
    elif choice == 9:
        dll.display_backward()
    elif choice == 10:
        break
    else:
        print("Invalid choice. Please try again.") 