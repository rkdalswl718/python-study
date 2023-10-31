def Max(list, len):
  if len == 1:
    return list[0]
  maxNum = Max(list, len-1)
  if maxNum > list[len-1]:
    return maxNum
  else:
    return list[len-1]

list = list(map(int,input().split()))

print(Max(list, len(list)))