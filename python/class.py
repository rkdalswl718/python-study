r,g,b = map(int,input().split())

for i in range (0, r):
    for j in range (0, g):
        for z in range (0, b):
            print(i,j,z)

print(r*g*b)