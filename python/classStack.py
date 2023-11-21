class Stack:
    def __init__(self, stack_size):   
        self.stack = [None] * stack_size #스택 초기화 
        self.top = -1 

    def is_empty(self):
        return self.top == -1 # top이 -1이면 스택이 비어있음.

    def is_full(self):
        return self.top == len(self.stack) - 1 #배열 마지막 요소가 top과 같으면 꽉참

    def push(self, e): #요소 추가 함수
        if self.is_full(): # 꽉차서 못넣을 때 overflow출력
            print('overflow')
        else:
            self.top += 1 # 꽉 안 차있으면 top 위에 +1
            self.stack[self.top] = e

    def pop(self): # 요소 제거 함수
        if self.is_empty(): # 비어있어서 더이상 지울 요소가 없을 때 underflow출력
            print('underflow')
        else:
            e = self.stack[self.top] # 요소 제거 후 반환
            self.top -= 1
            return e

    def peek(self):
        if not self.is_empty():
            print(self.stack) # 스택의 모든 요소 출력

    def get_min(self): # 스택의 모든 요소 중 가장 작은 요소 찾기
        if not self.is_empty():
            return min(self.stack[:self.top + 1])
    # 리스트 슬라이싱. 리스트 처음부터 self.top+1까지(현재요소 모두 포함)
    
    def get_max(self): # 스택의 모든 요소 중 가장 큰 요소 찾기
        if not self.is_empty():
            return max(self.stack[:self.top + 1])
        
    def get_sum(self): # 스택의 모든 요소를 다 더한 값 찾기
        if not self.is_empty():
            return sum(self.stack[:self.top + 1])

stack_size = 5
my_stack = Stack(stack_size)

my_stack.push(1)
my_stack.push(1)
my_stack.push(3)
my_stack.push(1)
my_stack.push(0)

print(my_stack.stack)
print('역순 출력:', my_stack.stack[::-1])
print('가장 작은 값:',my_stack.get_min())
print('가장 큰 값:',my_stack.get_max())
print('스택의 합:',my_stack.get_sum())