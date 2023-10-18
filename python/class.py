def 섹스(list):
    if list == []:
        return 0
    else:
        return list.pop() + 섹스(list)

li = list(map(int,input().split()))

print(섹스(li))