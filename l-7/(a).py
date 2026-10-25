class queuearray:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    #enqueue operation
    def enqueue(self, data):
        if self.rear == self.size - 1:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = data
            print(f"{data} enqueued to queue.")

    #dequeue operation
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            print(f"{item} dequeued from queue.")

            if self.front > self.rear:
                self.front = -1
                self.rear = -1
                
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
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])

class queuesll:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    #enqueue operation
    def enqueue(self, data):
        new = self.Node(data)
        if self.rear is None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        print(f"{data} enqueued to queue.")

    #dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(f"{item} dequeued from queue.")

    #peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(f"Front element is {self.front.data}.")

    #display operation
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Queue elements are:")
            while temp is not None:
                print(temp.data)
                temp = temp.next

q_arr =  queuearray(int(input("Enter size of queue(array):")))
q_sll = queuesll()
while True:
    print("1. Enqueue in array-based queue")
    print("2. Dequeue from array-based queue")
    print("3. Peek in array-based queue")
    print("4. Display array-based queue")
    print("5. Enqueue in linked list-based queue")
    print("6. Dequeue from linked list-based queue")
    print("7. Peek in linked list-based queue")
    print("8. Display linked list-based queue")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to enqueue:"))
        q_arr.enqueue(data)
    elif choice == 2:
        q_arr.dequeue()
    elif choice == 3:
        q_arr.peek()
    elif choice == 4:
        q_arr.display()
    elif choice == 5:
        data = int(input("Enter value to enqueue:"))
        q_sll.enqueue(data)
    elif choice == 6:
        q_sll.dequeue()
    elif choice == 7:
        q_sll.peek()
    elif choice == 8:
        q_sll.display()
    elif choice == 9:
        break
    else:
        print("Invalid choice")
