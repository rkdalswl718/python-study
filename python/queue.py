size = 23
queue = [None] * size
front = rear = 0
#front는 첫 요소 가리킴, rear은 맨 뒤 요소 가리킴. 추가, 제거시 rear이 바뀜

def isEmpty(): #비엇는지 확인
    return front == rear 

def isFull(): #꽉찼는지 확인    
    return (front == rear + 1) or (front == 0 and rear == size - 1)
#(front == rear + 1): front가 rear 다음에 위치할 때. 이는 큐의 모든 요소가 차있는 경우.
#(front == 0 and rear == size - 1): front가 큐의 맨 앞에 위치하고,rear가 큐의 맨 뒤에 위치할 때. 
# 이는 큐의 맨 끝과 맨 처음이 연결된 상태에서 큐가 모두 찬 경우입니다.

def enqueue(e):
    global rear
    if isFull():
        print("큐가 꽉 찼습니다")
    else:
        rear = (rear + 1) % size
        queue[rear] = e

def dequeue():
    global front
    if isEmpty():
        print("큐가 비어 있습니다")
    else:
        front = (front + 1) % size
        return queue[front]
    
def getQueue() :
    return queue[front +1 : rear + 1]

def getSize(): # 큐의 크기
    return (size - front + rear) % size if rear >= front else (rear - front + size) % size

def peek(): # 큐의 맨 앞의 원소를 반환하지만 큐에서 제거하지 않음
    if isEmpty():
        print("큐가 비어 있습니다")
    else:
        return queue[(front + 1) % size]

def clear():# 큐의 모든 원소 제거
    global front, rear
    front = rear = 0


enqueue(1)
enqueue(2)
enqueue(2)
enqueue(2)
enqueue(2)
enqueue(3)
dequeue()
dequeue()
dequeue()
dequeue()

print("list : ", getQueue())
# 큐의 크기 출력
print("Queue Size:", getSize())

# 큐의 맨 앞 원소 확인
print("Peek:", peek())

# 큐 비우기
clear()
print("Cleared Queue")

# 다시 큐에 원소 추가
enqueue(4)
enqueue(5)
enqueue(6)

# 큐의 내용 출력
print("Queue Content:", getQueue())
