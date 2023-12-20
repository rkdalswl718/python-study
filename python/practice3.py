class Queue:
    def __init__(self, queue_size=5):
        self.queue = [None] * queue_size
        self.front = self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % len(self.queue) == self.front

    def enqueue(self, e):
        if self.isFull():
            print("큐가 꽉 찼습니다.")
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = e

    def dequeue(self):
        if self.isEmpty():
            print("큐가 비어 있습니다.")
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

    def peek(self):
        if self.isEmpty():
            print("큐가 비어 있습니다.")
        else:
            return self.queue[(self.front + 1) % len(self.queue)]


queue = Queue()

queue.enqueue(6)
queue.enqueue(5)
queue.enqueue(6)

print(queue.peek())
