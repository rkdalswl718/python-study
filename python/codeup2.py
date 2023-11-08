def 이(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return 이(n // 2) + str(n % 2)

n = int(input())
print(이(n))
