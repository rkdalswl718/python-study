stack_size = 5
list = [None]*stack_size
top=-1

def isEmpty():
    return top == -1

def isFull():
    return top == stack_size -1

def push(e):
    global top
    if isFull():
        print('overFlow')
    else:
        top+=1
        list[top] = e
    

def pop(e):
    global top
    if isEmpty:
        print('underFlow')
    else:
        top-=1
        list[top] = e

def peek():
    if not isEmpty():
        print(list)

push(1)
push(1)
push(3)
push(1)
push(0)


print(list)