class Deque:
    def __init__(self):
        self.deque = []

    def isEmpty(self):
        return len(self.deque) == 0
    
    def isFull(self):
        return False
    
    def addFront(self, e):
        self.deque.insert(0,e)

    def deleteFront(self):
        if not self.isEmpty():
            return self.deque.pop(0)
        else :
            print('덱이 비엉ㅆ습니다')
            return None