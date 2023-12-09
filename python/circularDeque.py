class CircularDeque:
    def __init__(self, max_size):
        # 초기화: 덱을 나타내는 리스트, 덱의 크기, front와 rear 포인터, 최대 크기
        self.deque = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0
        self.max_size = max_size

    def isEmpty(self):
        # 덱이 비어있는지 확인
        return self.size == 0

    def isFull(self):
        # 덱이 가득 차 있는지 확인
        return self.size == self.max_size

    def addFront(self, e):
        # 맨 앞에 원소 추가
        if not self.isFull():
            self.front = (self.front - 1) % self.max_size
            self.deque[self.front] = e
            self.size += 1
            print('앞에서 추가:', e)
        else:
            print("덱이 가득 차 있습니다.")

    def deleteFront(self):
        # 맨 앞의 원소 삭제 및 반환
        if not self.isEmpty():
            front_value = self.deque[self.front]
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return front_value
        else:
            print("덱이 비어있습니다.")
            return None

    def getFront(self):
        # 맨 앞의 원소 반환 (꺼내지 않음)
        if not self.isEmpty():
            return self.deque[self.front]
        else:
            print("덱이 비어있습니다.")
            return None

    def addRear(self, e):
        # 맨 뒤에 원소 추가
        if not self.isFull():
            self.deque[self.rear] = e
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1
            print('뒤에서 추가:', e)
        else:
            print("덱이 가득 차 있습니다.")

    def deleteRear(self):
        # 맨 뒤의 원소 삭제 및 반환
        if not self.isEmpty():
            self.rear = (self.rear - 1) % self.max_size
            rear_value = self.deque[self.rear]
            self.size -= 1
            return rear_value
        else:
            print("덱이 비어있습니다.")
            return None

    def getRear(self):
        # 맨 뒤의 원소 반환 (꺼내지 않음)
        if not self.isEmpty():
            return self.deque[(self.rear - 1) % self.max_size]
        else:
            print("덱이 비어있습니다.")
            return None


# 덱 생성 (최대 크기: 5)
max_size = 5
myCircularDeque = CircularDeque(max_size)

# 덱에 원소 추가
myCircularDeque.addFront(1)
myCircularDeque.addFront(2)
myCircularDeque.addRear(3)
myCircularDeque.addRear(4)
myCircularDeque.addRear(5)

print("덱:", myCircularDeque.deque)

# 맨 앞과 맨 뒤의 원소를 삭제하고 출력
print("deleteFront():", myCircularDeque.deleteFront())
print("deleteRear():", myCircularDeque.deleteRear())
print("deleteRear():", myCircularDeque.deleteRear())
print("deleteRear():", myCircularDeque.deleteRear())

print("덱:", myCircularDeque.deque)

# 맨 앞과 맨 뒤의 원소를 반환 (꺼내지 않음)
print("getFront():", myCircularDeque.getFront())
print("getRear():", myCircularDeque.getRear())
