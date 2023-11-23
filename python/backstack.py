stack_size = 100

class Stack:
  def __init__(self):
    self.list = [] * stack_size

  def isEmpty(self):
    if len(self.list):
      return False
    else:
      return True

  def isFull(self):
    if len(self.list) == stack_size:
      return False
    else:
      return True

  def push(self, data):
    if self.isFull():
      self.list.append(data)
    else:
      print("Stack is Full")

  def pop(self):
    if not self.isEmpty():
      return self.list.pop()
    else:
      print("Stack is Empty")

  def peek(self):
    if self.isEmpty():
      print("Stack is Empty.")
    else:
      return self.list[-1]

  def F(self, x):
    op = {"+": 1, "-": 1, "*": 2, "/": 2}
    result = []
    for i in x:
      if i.isnumeric():
        result.append(i)
        print("append 1")
      elif i == "(":
        self.push(i)
      elif i == ")":
        while self.peek() != "(":
          result.append(self.pop())
          print("append 2")
        self.pop()
      elif i in op:
        if self.list and self.peek() != "(" and (op[i] <= op[self.peek()]):
          result.append(self.pop())
          print("append 3")
        self.push(i)
    while self.list:
      result.append(self.pop())
      print("append 4")
    print(''.join(result))


S = Stack()
S.F('1+(2+3)')
