def SumList(data): #이거머임
  if data == []: 
    return 0
  else:
    return data[0] + SumList(data[1:])

li = list(map(int,input().split()))
#[1, 2, 3, 4, 5]

print(SumList(li))
