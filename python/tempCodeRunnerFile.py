def is_palindrome(num):
    # 숫자를 문자열로 변환하여 회문 여부를 판단
    num_str = str(num)
    return num_str == num_str[::-1]

def reverse_and_add(num):
    # 주어진 숫자를 뒤집어서 더하고 결과를 반환
    num_str = str(num)
    reversed_num_str = num_str[::-1]
    reversed_num = int(reversed_num_str)
    return num + reversed_num

def is_valid_password(num):
    # 뒤집어 더하기를 반복하며 회문을 찾을 때까지 확인
    for _ in range(100):
        num = reverse_and_add(num)
        if is_palindrome(num):
            return True
    return False

# 사용자로부터 숫자를 입력받음
num = int(input())

# 입력 숫자가 정상적인 뒤집어 더하기 암호인지 판단
if is_valid_password(num):
    print("YES")
else:
    print("NO")
