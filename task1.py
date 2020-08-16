# Возможно в примере входных данных есть опечатка в первой строке "а3",
# делаю вариант, если учитывать входные, как в описании задачи и в первой строке дано только число N
# 3
# x . 0
# x 0 x
# 0 . .

def checkLine(i, j):
    k = 0
    for y in range(1, n):
        if arr[i][y] == arr[i][y-1] and arr[i][y] in "x0":
            k += 1
    if k == n - 1:
        return True
    return False

def checkColumn(i, j):
    k = 0
    for x in range(1, n):
        if arr[x][j] == arr[x-1][j] and arr[x][j] in "x0":
            k += 1
    if k == n - 1:
        return True
    return False

def checkDiagonalZero():
    k = 0
    for x in range(1, n):
        for y in range(1, n):
            if arr[x][y] == arr[x-1][y-1] and arr[x][y] in "x0":
                k += 1
    if k == n - 1:
        return True
    return False

def checkDiagonalN():
    k = 0
    y = n - 2
    for x in range(1, n):
        if arr[x][y] == arr[x-1][y+1] and arr[x][y] in "x0":
            k += 1
        y -= 1
    if k == n - 1:
        return True
    return False

n = int(input())
if n == 0:
    print("Error: N = 0")
elif n == 1:
    print(input())
else:
    key = False
    arr = [input().split() for i in range(n)]
    for i in range(0, n):
        if checkLine(i, 0):
            print(arr[i][0])
            key = True
        if key:
            break
    if not key:
        for j in range(0, n):
            if checkColumn(0, j):
                print(arr[0][j])
                key = True
            if key:
                break
    if not key:
        if checkDiagonalZero():
            print(arr[0][0])
            key = True
    if not key:
        if checkDiagonalN():
            print(arr[0][n-1])
            key = True
    if not key:
        print("x0")
