n = int(input())  # n = 3
a = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        print(a[(i+j)%n],end=' ')
    print()
    