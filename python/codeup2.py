d = [[0] * 20 for _ in range (20)]
n = int(input())
for i in range (n):
    x,y = map(int,input().split())
    d[x][y]=1

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
    print()