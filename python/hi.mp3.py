board = []

for i in range(19) :
    row = []      #리스트 안에 다른 리스트 추가해 넣기
    for j in range(19) : 
        row.append(0)
        board.append(row)

n = int(input())

# 흰 돌의 위치를 입력 받아 해당 위치에 흰 돌 놓기
for i in range(n):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1   # 좌표는 1부터 시작하지만 인덱스는 0부터 시작하므로 -1

#바둑판 출력하기
for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ') 

print()