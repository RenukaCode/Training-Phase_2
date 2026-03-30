#================ Stack ================
class Stack:
    def __init__(self, size):
        self.stack = [0]*size
        self.top = -1
        self.size = size
    def is_full(self):
        return self.top + 1 == self.size
    def push(self,data):
        if self.is_full():
            print("Overflow")
            return 
        self.top += 1
        self.stack[self.top] = data
    def pop(self, data):
        if self.top == -1:
            print("Underflow")
            return 
        self.top -= 1
    def peek(self):
        if self.top == -1:
            print("Underflow")
            return
        print(self.stack[self.top])
    def display(self):
        if self.top == -1:
            print("Underflow")
            return
        for i in range(self.top,-1,-1):
            print(self.stack[i], end = " ")   
s = Stack(4)
s.push(2)
s.push(5)
s.push(6)
s.push(7)
s.display()  # [7 6 5 2]

#=====Py code
stack = []
stack.append(0)
stack.pop()
print(stack[-1])
print(len(stack)==0)
#===========




#================== QUEUE ==================
class Queue:
    def __init__(self,size):
        self.queue = []*size
        self.front = -1
        self.rear = -1
        self.size = size
    def enqueue(self, data):
        if self.rear+1 == self.size:
            print("Is full")
            return 
        if self.front == -1:
            self.front += 1
        self.rear += 1
        self.queue[self.rear] = data
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("empty")
            return
        self.front += 1
    def peek(self, data):
        if self.front == -1 or self.front > self.rear:
            print("empty")
            return
        print(self.queue[self.front])
    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("empty")
            return
        for i in range(self.front, self.rear+1):
            print(self.queue[i], end = " ")      
q = Queue(4)
q.dequeue()
print()
q.display()  

#======Py code
queue = []
queue.qppend(7)
queue.insert(0,7)
queue.pop(0)
queue.pop()
print(queue[0])
print(len(queue) == 0)
#=======