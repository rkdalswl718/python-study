def 팩(n):
    if n ==0:
        return 1
    else:
        return n*팩(n-1)
n = (int(input()))
print(팩(n))