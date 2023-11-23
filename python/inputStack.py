class Stack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list = [None] * stack_size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.stack_size - 1

    def push(self, e):
        if self.isFull():
            print('Overflow')
        else:
            self.top += 1
            self.list[self.top] = e

    def pop(self):
        if self.isEmpty():
            print('Underflow')
        else:
            popped_element = self.list[self.top]
            self.top -= 1
            return popped_element

    def peek(self):
        if not self.isEmpty():
            print(self.list)


def main() :
    stack_size = int(input())
    stack = Stack(stack_size)

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. 종료")

        choice = input("원하는 작업을 선택하세요 (1-4): ")

        
        if choice == '1':
            element = input("추가할 요소를 입력하세요: ")
            stack.push(element)
        elif choice == '2':
            popped_element = stack.pop()
            if popped_element is not None:
                print(f"Pop된 요소: {popped_element}")
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해 주세요.")


if __name__ == "__main__":
    main()
