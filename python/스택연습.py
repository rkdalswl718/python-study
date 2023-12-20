class Stack :
    def __init__(self, stack_size = 5):
        self.stack = [None] * stack_size
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == len(self.stack) -1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('꽉 차서 못 넣는다')

    def pop(self):
        if not self.isEmpty() :
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            ("비어잇어서 삭제시킬게없음")

    def peek(self):
        if not self.isEmpty():
            print(self.stack[self.top])

stack = Stack()

stack.push(2342)
stack.push(9)
stack.push(2)
stack.push(263)

stack.peek()

stack.push(100)
stack.push(91)
stack.push(101)

stack.pop()
stack.peek()
