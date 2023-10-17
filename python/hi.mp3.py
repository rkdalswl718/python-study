def 응애(list):
    if not list:  
        return
    print(list.pop())
    응애(list) 

list = list(map(int,input().split()))

응애(list)