def createQueue(size):  
    queue = [None] * size
    front = rear = 0

    def isEmpty(): 
        return front == rear 

    def isFull(): 
        return (front == rear + 1) or (front == 0 and rear == size - 1)

    def enqueue(e):
        nonlocal rear
        if isFull():
            print("큐가 꽉 찼습니다")
        else:
            rear = (rear + 1) % size
            queue[rear] = e

    def dequeue():
        nonlocal front
        if isEmpty():
            print("큐가 비어 있습니다")
        else:
            front = (front + 1) % size
            return queue[front]
        
    def getQueue():
        return queue[front +1: rear + 1]

    return enqueue, dequeue, getQueue

enqueue, dequeue, getQueue = createQueue(5)

enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
enqueue(6)

print("list:", getQueue())
