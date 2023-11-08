def 앙(a,b):
    if(a>b):
        return
    if a%2==1:
        print(a,end=' ')
    앙(a+1,b)

a,b=(map(int,input().split()))
앙(a,b)