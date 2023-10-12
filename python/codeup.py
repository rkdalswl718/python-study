def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_valid_password(num):
        num_str = str(num)
        reversed_num_str = num_str[::-1]
        num = int(num_str) + int(reversed_num_str)
        if is_palindrome(num):
            return "YES"
        return "NO"

num = int(input())

print(is_valid_password(num))
