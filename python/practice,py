class Stack:
    def __init__(self, Stack_size = 5):
        self.stack = [None] * Stack_size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == len(self.stack) - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print("다 차있음")

    def pop(self):
        if self.isFull():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print("더이상지울게없노이기야")

    def peek(self):
        if not self.isEmpty():
            print(self.stack[self.top])


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(434534)

stack.peek()
