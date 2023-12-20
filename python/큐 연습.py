class Queue:
    def __init__ (self, queue_size = 5):
        self.queue = [None] * queue_size
        self.front = self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % len(self.queue)
    
    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = e
    
    def dequeue(self)


queue = Queue()

queue.enqueue(6)
queue.enqueue(5)
queue.enqueue(6)

print(queue.peek())
