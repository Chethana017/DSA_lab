class circular_linked_list:
    #creating a node 
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    #initializing the head and tail 
    def __init__(self):
        self.head = None
        self.tail = None

    #adding a node to the list
    def create(self):   
        n = int(input("Enter number of elements:"))
        for i in range(n):
            x = int(input("Enter value:"))
            new = self.Node(x)
            if self.head is None:
                self.head = new
                self.tail = new
                new.next = self.head
            else:
                self.tail.next = new
                self.tail = new
                self.tail.next = self.head

    #insertion in cll-at the beginning
    def insert_beginning(self, data):
        new = self.Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
            new.next = self.head
        else:
            new.next = self.head
            self.head = new
            self.tail.next = self.head    

    #insertion in cll-at the end
    def insert_end(self, data):
        new = self.Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
            new.next = self.head
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head
    
    #insertion in cll-at a given position
    def insert_position(self, position, data):
        if position == 0:
            self.insert_beginning(data) 
            return
        
        if self.head is None or position < 0:
            print("Invalid position")
            return

        new = self.Node(data)
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
            if temp == self.head:
                print("Invalid position")
                return

        new.next = temp.next
        temp.next = new 

        if temp == self.tail:
            self.tail = new

    #deletion in cll-at the beginning
    def delete_beginning(self):
        if self.head is None:
            print("No elements to delete")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            self.tail.next = self.head

    #deletion in cll-at the end
    def delete_end(self):
        if self.head is None:
            print("No elements to delete")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = self.head
        self.tail = temp

    #traversing the list
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")
    
    #display head and tail
    def display_head_tail(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Head = ", self.head.data)
            print("Tail = ", self.tail.data)

cll = circular_linked_list()
while True:
    print("1. Create a circular linked list")
    print("2. Insert at the beginning")
    print("3. Insert at the end")
    print("4. Insert at a given position")
    print("5. Delete from the beginning")
    print("6. Delete from the end")
    print("7. Traverse the list")
    print("8. Display head and tail")
    print("9. Exit")
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        cll.create()
    elif choice == 2:
        data = int(input("Enter value to insert:"))
        cll.insert_beginning(data)
    elif choice == 3:
        data = int(input("Enter value to insert:"))
        cll.insert_end(data)
    elif choice == 4:
        position = int(input("Enter position to insert:"))
        data = int(input("Enter value to insert:"))
        cll.insert_position(position, data)
    elif choice == 5:
        cll.delete_beginning()
    elif choice == 6:
        cll.delete_end()
    elif choice == 7:
        cll.traverse()
    elif choice == 8:
        cll.display_head_tail()
    elif choice == 9:
        break