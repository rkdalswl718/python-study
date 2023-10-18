def 시발(list) :
    if list == [] :
        return
    else :
        return(max(list))

list = list(map(int,input().split()))

최고 = 시발(list)
print(최고)