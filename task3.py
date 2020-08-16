# 10
# _ _ _ _ _ _ _ _ _ _
# _ _ _ _ _ _ _ _ _ _
# _ x _ _ _ _ _ . . .
# _ . _ _ _ _ _ . _ _
# _ . _ _ . . . . _ _
# _ . _ _ . _ _ _ _ _
# _ . _ _ . _ _ _ _ _
# _ . . . . _ _ _ _ _
# _ _ _ _ _ _ _ _ _ _
# _ _ _ _ _ _ _ _ _ _

def findPos(field, n):
    for i in range(n):
        for j in range(n):
            if field[i][j] == 'x':
                return i, j

def findWay(field, n, i, j, iLast, jLast):
    if field[i-1][j] == '.' and i-1 != iLast:
        print('Наверх!')
        return i, j, i-1, j
    if field[i][j-1] == '.' and j-1 != jLast:
        print('Налево!')
        return i, j, i, j-1
    if field[i][j+1] == '.' and j+1 != jLast:
        print('Направо!')
        return i, j, i, j+1
    if field[i+1][j] == '.' and i+1 != iLast:
        print('Вниз!')
        return i, j, i+1, j

n = int(input())
field = [input().split() for i in range(n)]

iPos, jPos = findPos(field, n)
iLast, jLast, i, j = findWay(field, n, iPos, jPos, -1, -1)
while True:
    iLast, jLast, i, j = findWay(field, n, i, j, iLast, jLast)
    if i == 0 or i == n-1 or j == 0 or j == n-1:
        break
