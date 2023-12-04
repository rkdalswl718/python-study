class Stack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.list[self.top] = e
        else:
            print("스택이 가득 참")

    def pop(self):
        if not self.isEmpty():
            popped_element = self.list[self.top]
            self.top -= 1
            return popped_element 
        else:
            print("스택이 비었다")
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.list[self.top]
        else:
            print("스택이 비었다")
            return None
        
    def input_push(self):
        e = input("입력할 값을 입력하세요: ")
        self.push(e)


def 우선순위(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def Infix2Postfix(expression):
    s = Stack()
    result = ''

    for char in expression:
        if char.isalnum():
            result += char
        elif char == '(':
            s.push(char)
        elif char == ')':
            while not s.isEmpty() and s.peek() != '(':
                result += s.peek()
                s.pop()
            s.pop()  
        else: 
            while not s.isEmpty() and 우선순위(char) <= 우선순위(s.peek()):
                result += s.peek()
                s.pop()
            s.push(char)

    while not s.isEmpty():
        if s.peek() == '(':
            s.pop()
        else:
            result += s.peek()
            s.pop()

    return result

infix_expression = "a+b*c-(d/e+f*g*h)"
postfix_expression = Infix2Postfix(infix_expression)
print("후위 표기법:", postfix_expression)