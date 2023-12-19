class Stack:
    def __init__(self, stack_size = 5):
        self.stack = [None] * stack_size
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == len(self.stack) -1
    
    def push(self, e):
        if not self.isFull() :
            self.top += 1
            self.stack[self.top] = e
        else:
            print('넣을 수 없습닏 꽉찻습니다?')

    def pop(self):
        if not self.isEmpty():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print('없어서 못뺌')

    def peek(self):
        if not self.isEmpty():
            print(self.stack[self.top])