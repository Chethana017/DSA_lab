class circularqueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    #enqueue operation
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print(f"{data} enqueued to queue.")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(f"{data} enqueued to queue.")

    #dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            print(f"{item} dequeued from queue.")
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            print(f"{item} dequeued from queue.")

    #peek operation
    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print(f"Front element is {self.queue[self.front]}.")

    #display operation
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements are:")
            i = self.front
            while True:
                print(self.queue[i])
                if i == self.rear:
                    break
                i = (i + 1) % self.size

size = int(input("Enter size of circular queue:"))
cq = circularqueue(size)
while True:
    print("1. enqueue")
    print("2. dequeue")
    print("3. peek")
    print("4. display")
    print("5. exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to enqueue:"))
        cq.enqueue(data)
    elif choice == 2:
        cq.dequeue()
    elif choice == 3:
        cq.peek()
    elif choice == 4:
        cq.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")