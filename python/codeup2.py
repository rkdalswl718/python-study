n = int(input())

while n >= 10:
    n = sum(map(int, str(n)))

print(n)
