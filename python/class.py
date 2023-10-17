def 재기(n) :
    if n!=0:
        재기(n-1)
        print([n::-1])
        

재기(int(input()))