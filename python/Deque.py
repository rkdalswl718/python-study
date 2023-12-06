class Deque:
    def __init__(self):
        # 덱을 리스트로 구현
        self.deque = []

    def isEmpty(self):
        # 덱이 비어있으면 True, 아니면 False 반환
        return len(self.deque) == 0

    def isFull(self):
        # 리스트의 크기를 제한하지 않기 때문에 항상 False를 반환
        return False

    def addFront(self, e):
        # 맨 앞에 원소 추가
        self.deque.insert(0, e)

    def deleteFront(self):
        # 맨 앞의 원소를 꺼내 반환
        if not self.isEmpty():
            return self.deque.pop(0)
        else:
            print("덱이 비어있습니다.")
            return None

    def getFront(self):
        # 맨 앞의 원소를 반환 (꺼내지 않음)
        if not self.isEmpty():
            return self.deque[0]
        else:
            print("덱이 비어있습니다.")
            return None

    def addRear(self, e):
        # 맨 뒤에 원소 추가
        self.deque.append(e)

    def deleteRear(self):
        # 맨 뒤의 원소를 꺼내 반환
        if not self.isEmpty():
            return self.deque.pop()
        else:
            print("덱이 비어있습니다.")
            return None

    def getRear(self):
        # 맨 뒤의 원소를 반환 (꺼내지 않음)
        if not self.isEmpty():
            return self.deque[-1]
        else:
            print("덱이 비어있습니다.")
            return None


# 덱 생성
myDeque = Deque()

# 덱에 원소 추가
myDeque.addFront(1)
myDeque.addFront(2)
myDeque.addRear(3)
myDeque.addRear(4)

print("덱:", myDeque.deque)

# 맨 앞과 맨 뒤의 원소를 삭제하고 출력
print("deleteFront():", myDeque.deleteFront())
print("deleteRear():", myDeque.deleteRear())

print("덱:", myDeque.deque)

# 맨 앞과 맨 뒤의 원소를 반환 (꺼내지 않음)
print("getFront():", myDeque.getFront())
print("getRear():", myDeque.getRear())
