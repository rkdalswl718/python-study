a,r,n=map(int, input().split())

print(a*r**(n-1))a,m,d,n = map(int,input().split())
num=0

for i in range(1,n):
    a = (m*a)+d
    
print(a)
