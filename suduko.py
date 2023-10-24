board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    row, col= find_empty(bo)
    if row==None:
        return True

    for i in range(1,10):
        if valid(bo, i, row, col):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo,number,row,col):
    for i in range(9):
        #row
        if bo[row][i]==number :
            return False
        #column
        if bo[i][col]==number:
            return False
        
    #grid
    grow=(row//3)*3
    gcol=(col//3)*3
    for i in range(grow,grow+3):
        for j in range(gcol,gcol+3):
            if bo[i][j]==number and (row!=i and col!=j):
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None,None

print_board(board)
solve(board)
print("___________________")
print_board(board)