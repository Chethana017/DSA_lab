class stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        
    #push operation
    def push(self, data):
        new = self.Node(data)
        new.next = self.top
        self.top = new
        print(f"{data} pushed to stack.")

    #pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        else:
            temp = self.top
            self.top = self.top.next
            print(f"{temp.data} popped from stack.")
            return temp.data
    
    #peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(f"Top element is {self.top.data}.")

    #display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements are:")
            while temp is not None:
                print(temp.data)
                temp = temp.next

s = stack()
while True:
    print("1. push")
    print("2. pop")
    print("3. peek")
    print("4. display")
    print("5. exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to push:"))
        s.push(data)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        break        
    else:
        print("Invalid choice. Please try again.")