class stack:
    #initializing stack
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    #push operation
    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = data
            print(f"{data} pushed to stack.")

    #pop operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"{item} popped from stack.")

    #peek operation
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"Top element is {self.stack[self.top]}.")
    
    #display operation
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

#creating stack object
size = int(input("Enter size of stack:"))
s = stack(size)
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
        print("Invalid choice.")