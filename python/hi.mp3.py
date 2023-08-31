d=[] #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기

for i in range(20) :
    d.append([])         #리스트 안에 다른 리스트 추가해 넣기
    for j in range(20) : 
        d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기

n = int(input())

for i in range(n) :
    x,y=input().split()
    for j in range(1, 20) :
        if d[j][int(y)]==0 :
            d[j][int(y)]=1
    else :
        d[j][int(y)]=0

    if d[int(x)][j]==0 :
        d[int(x)][j]=1
    else :
        d[int(x)][j]=0

for i in range(1, 20) :
    for j in range(1, 20) : 
        print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
print()            