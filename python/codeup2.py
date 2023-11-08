n = int(input())
cnt = 0
for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
    if n//i != 0:
        cnt += n//i
        n = n%i
print(cnt)