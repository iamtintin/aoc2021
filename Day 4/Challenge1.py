def win(board):
    row = [0, 0, 0, 0, 0]
    column = [0, 0, 0, 0, 0]
    unmarked = []
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j].startswith('x'):
                row[i] = 1 + row[i]
                column[j] = 1 + column[j]
            else:
                unmarked.append(board[i][j])
    
    if 5 in row or 5 in column:
        return sum([int(x) for x in unmarked])
    else:
        return -1

def mark(board, key):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == key:
                board[i][j] = "x" + board[i][j]
    return board

with open("input.txt") as txtFile:
    data = txtFile.readlines()

numbers = data[0].strip("\n").split(',')
numbers = [x for x in numbers]

data.pop(0)

rows = []

for i in range(0, len(data)):
    if data[i] != '\n':
        row = data[i].strip('\n').split(' ')
        row = [x for x in row if x != '']
        rows.append(row)

boards = []

for i in range(0, len(rows), 5):
    boards.append(rows[i:i+5])

for i in range(0, len(numbers)):
    for x in range(0, len(boards)):
        boards[x] = mark(boards[x], numbers[i])
        check = win(boards[x])
        if check != -1:
            print(int(numbers[i]) * check)
            break
    if check != -1:
        break