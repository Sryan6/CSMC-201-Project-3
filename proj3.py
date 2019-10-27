# File:    proj3.py
# Author:  Steven Ryan
# Date:    12/5/18
# Section: 34
# E-mail:  sryan6@umbc.edu
# Description:
#    Plays a game of sudoku and solves it

# Constants:
BOARD_LENGTH = 9
PLAY = "p"
SOLVE = "s"
SAVE = "s"
UNDO = "u"
QUIT = "q"
YES = "y"
NO = "n"
VALUE_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ELIMINATION = 4
DEEP_COPY_CONSTANT = 2
#constants for the squares of the sudoku board
ROW_COLUMN_1 = 2
ROW_COLUMN_2 = 5
ROW_COLUMN_3 = 8

# prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;   the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ") 
    print("  +-------+-------+-------+")

    for i in range(len(board)): 
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i]) 
        for j in range(len(boardRow)):
            if boardRow[j] == 0:
                boardRow[j] = "_"

        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1, 
                boardRow[0], boardRow[1], boardRow[2], 
                boardRow[3], boardRow[4], boardRow[5], 
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
# Output:      fileName; the string of the file to use for writing to 
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()

# readFile() reads the file line by line and places it into a list
# 
# Input:     fileName; the name of the string to read
# Output:    board; the 2d list to append with the values
def readFile(fileName):
    file = open(fileName, "r")
    board = []
    for i in range(0, BOARD_LENGTH):
        boardLine = []
        boardLine = file.readline()
        boardLine = boardLine.strip()
        boardLine = boardLine.split(",")
        board.append(boardLine)
    file.close()
    return board

# solve() creates a solution for the board
# 
# Input:  board; a 2d list to solve.
#         row; the current row. col; the current column
#         boardValues, the 3d list of values for each coordinate.
# Output: boolean; the boolean that determines when it's solved
def solve(board, row, col, boardValues):
    exitflag = True
    for y in range(0, len(board)):
        for t in range(0, len(board[y])):
            if(board[y][t] == 0):
                exitflag = False
    if(exitflag == True):
        print("", end = "")
        return True
    else:
        if(board[row][col] == 0):
            possValues = list(VALUE_LIST)
            
            #checks columns
            for i in range(0, len(board)):
                if(board[row][i] != 0 and board[row][i] in possValues):
                    possValues.remove(board[row][i])
            #checks rows
            for u in range(0, len(board[row])):
                if(board[u][col] != 0 and board[u][col] in possValues):
                    possValues.remove(board[u][col])
            #checks squares
            #Square1
            if(row <= ROW_COLUMN_1 and col <= ROW_COLUMN_1):
                for q in range(0, ROW_COLUMN_1 + 1):
                    for w in range(0, ROW_COLUMN_1 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                            
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(0, ROW_COLUMN_1 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(0, ROW_COLUMN_1 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
                        
            #Square2
            elif(row <= ROW_COLUMN_1 and col > ROW_COLUMN_1
                 and col <= ROW_COLUMN_2):
                for q in range(0, ROW_COLUMN_1 + 1):
                    for w in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(0, ROW_COLUMN_1 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
            #Square3
            elif(row <= ROW_COLUMN_1 and col > ROW_COLUMN_2
                 and col <= ROW_COLUMN_3):
                for q in range(0, ROW_COLUMN_1 + 1):
                    for w in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(0, ROW_COLUMN_1 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
                    
            #Square4
            elif(row > ROW_COLUMN_1 and row <= ROW_COLUMN_2
                 and col <= ROW_COLUMN_1):
                
                for q in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                    for w in range(0, ROW_COLUMN_1 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(0, ROW_COLUMN_1 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
            #Square5
            elif(row > ROW_COLUMN_1 and row <= ROW_COLUMN_2
                 and col > ROW_COLUMN_1 and col <= ROW_COLUMN_2):
                for q in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                    for w in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
            #Square6
            elif(row > ROW_COLUMN_1 and row <= ROW_COLUMN_2
                 and col > ROW_COLUMN_2 and col <= ROW_COLUMN_3):
                for q in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                    for w in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
            #Square7
            elif(row > ROW_COLUMN_2 and row <= ROW_COLUMN_3
                 and col <= ROW_COLUMN_1):
                for q in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                    for w in range(0, ROW_COLUMN_1 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(0, ROW_COLUMN_1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
            #Square8
            elif(row > ROW_COLUMN_2 and row <= ROW_COLUMN_3
                 and col > ROW_COLUMN_1 and col <= ROW_COLUMN_2):
                for q in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                    for w in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
            #Square9
            elif(row > ROW_COLUMN_2 and row <= ROW_COLUMN_3
                 and col > ROW_COLUMN_2 and col <= ROW_COLUMN_3):
                for q in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                    for w in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(board[q][w] != 0 and board[q][w] in possValues):
                            possValues.remove(board[q][w])
                for g in range(0, len(possValues)):
                    counter = 0
                    #checks rows for solving by elimination
                    for c in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(row != c):
                            for p in range(0, BOARD_LENGTH):
                                if(board[c][p] == possValues[g]):
                                    counter += 1
                    #checks columns for solving by elimination
                    for x in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                        if(col != x):
                            for v in range(0, BOARD_LENGTH):
                                if(board[v][x] == possValues[g]):
                                    counter += 1
                    if(counter == ELIMINATION):
                        board[row][col] = possValues[g]
                        
            if(len(possValues) == 1):
                board[row][col] = possValues[0]

        #Works with the possible values list
        elif(board[row][col] != 0):
            possValues = [board[row][col]]
        if(boardValues[row][col] != tuple(possValues)):
            boardValues[row][col] = tuple(possValues)

        if(row == BOARD_LENGTH - 1 and col == BOARD_LENGTH - 1
           and exitflag != True):

            #Extra algorithm for solving puzzleD
            #Square1
            puzzleDSolver(boardValues, board, 0, ROW_COLUMN_1 + 1,
                          0, ROW_COLUMN_1 + 1)
            #Square2
            puzzleDSolver(boardValues, board, 0, ROW_COLUMN_1 + 1,
                          ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1)
            #Square3
            puzzleDSolver(boardValues, board, 0, ROW_COLUMN_1 + 1,
                          ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1)
            #Square4
            puzzleDSolver(boardValues, board, ROW_COLUMN_1 + 1,
                          ROW_COLUMN_2 + 1, 0, ROW_COLUMN_1 + 1)
            #Square5
            puzzleDSolver(boardValues, board, ROW_COLUMN_1 + 1,
                          ROW_COLUMN_2 + 1, ROW_COLUMN_1 + 1,
                          ROW_COLUMN_2 + 1)
            #Square6
            puzzleDSolver(boardValues, board, ROW_COLUMN_1 + 1,
                          ROW_COLUMN_2 + 1, ROW_COLUMN_2 + 1,
                          ROW_COLUMN_3 + 1)
            #Square7
            puzzleDSolver(boardValues, board, ROW_COLUMN_2 + 1,
                          ROW_COLUMN_3 + 1, 0, ROW_COLUMN_1 + 1)
            #Square8
            puzzleDSolver(boardValues, board, ROW_COLUMN_2 + 1,
                          ROW_COLUMN_3 + 1, ROW_COLUMN_1 + 1,
                          ROW_COLUMN_2 + 1)
            #Square9
            puzzleDSolver(boardValues, board, ROW_COLUMN_2 + 1,
                          ROW_COLUMN_3 + 1, ROW_COLUMN_2 + 1,
                          ROW_COLUMN_3 + 1)
                        
            solve(board, 0, 0, boardValues)
            
        elif(col == BOARD_LENGTH - 1 and exitflag != True):
            solve(board, row + 1, 0, boardValues)
        elif(exitflag != True):
            solve(board, row, col + 1, boardValues)            

# puzzleDSolver() extra algorithm to solve puzzleD each square
#                 at a time.
# Input:  boardValues; 3d tuple list with possible values for the board
#         board; 2d list that will change if the conditions are met
#         rowMin, rowMax; integer bounds for the row of the square
#         colMin, colMax; integer bounds for the column of the square
# Output: nothing, it just changes the board if there is a number
#         where there is only one possibility within the square
def puzzleDSolver(boardValues, board, rowMin, rowMax, colMin, colMax):
    square = []
    removeList = []
    for q in range(rowMin, rowMax):
        for w in range(colMin, colMax):
            for b in range(0, len(boardValues[q][w])):
                if(boardValues[q][w][b] in square):
                    removeList.append(boardValues[q][w][b])
                square.append(boardValues[q][w][b])
    for q in range(0, len(removeList)):
        while(removeList[q] in square):
            square.remove(removeList[q])
    for q in range(rowMin, rowMax):
        for w in range(colMin, colMax):
            for c in range(0, len(square)):
                if(square[c] in boardValues[q][w]):
                    board[q][w] = square[c]

# castInt() casts a list of values as integers
# 
# Input:  board; a 2d list to solve.
# Output: board; the 2d list solved board
def castInt(board):
    for i in range(0, BOARD_LENGTH):
        for u in range(0, BOARD_LENGTH):
            board[i][u] = int(board[i][u])
    return board

# validateNumber() makes sure a number is not ruled out as an option
# 
# Input:  board; the 2d list board to play with,
#         num; the integer to manipulate
#         row; the integer row to test,
#         col; the integer column to test
# Output: valid; a boolean that says whether it's valid or not
def validateNumber(board, num, row, col):
    if(num > 9 or num < 1):
        return False
    #checks columns
    for i in range(0, len(board)):
        if(board[row][i] == num):
            print("There is another", str(num), "in column")
            return False
    #checks rows
    for u in range(0, len(board[row])):
        if(board[u][col] == num):
            return False
    #checks squares
    #Square1
    if(row <= ROW_COLUMN_1 and col <= ROW_COLUMN_1):
        for q in range(0, ROW_COLUMN_1):
            for w in range(0, ROW_COLUMN_1):
                if(board[q][w] == num):
                    return False
    #Square2
    elif(row <= ROW_COLUMN_1 and col > ROW_COLUMN_1
         and col <= ROW_COLUMN_2):
        for q in range(0, ROW_COLUMN_1):
            for w in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                if(board[q][w] == num):
                    return False
    #Square3
    elif(row <= ROW_COLUMN_1 and col > ROW_COLUMN_2
         and col <= ROW_COLUMN_3):
        for q in range(0, ROW_COLUMN_1):
            for w in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                if(board[q][w] == num):
                    return False
    #Square4
    elif(row > ROW_COLUMN_1 and row <= ROW_COLUMN_2
         and col <= ROW_COLUMN_1):
        for q in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
            for w in range(0, ROW_COLUMN_1):
                if(board[q][w] == num):
                    return False
    #Square5
    elif(row > ROW_COLUMN_1 and row <= ROW_COLUMN_2
         and col > ROW_COLUMN_1 and col <= ROW_COLUMN_2):
        for q in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
            for w in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                if(board[q][w] == num):
                    return False
    #Square6
    elif(row > ROW_COLUMN_1 and row <= ROW_COLUMN_2
         and col > ROW_COLUMN_2 and col <= ROW_COLUMN_3):
        for q in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
            for w in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                if(board[q][w] == num):
                    return False
    #Square7
    elif(row > ROW_COLUMN_2 and row <= ROW_COLUMN_3
         and col <= ROW_COLUMN_1):
        for q in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
            for w in range(0, ROW_COLUMN_1):
                if(board[q][w] == num):
                    return False
    #Square8
    elif(row > ROW_COLUMN_2 and row <= ROW_COLUMN_3
         and col > ROW_COLUMN_1 and col <= ROW_COLUMN_2):
        for q in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
            for w in range(ROW_COLUMN_1 + 1, ROW_COLUMN_2 + 1):
                if(board[q][w] == num):
                    return False
    #Square9
    elif(row > ROW_COLUMN_2 and row <= ROW_COLUMN_3
         and col > ROW_COLUMN_2 and col <= ROW_COLUMN_3):
        for q in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
            for w in range(ROW_COLUMN_2 + 1, ROW_COLUMN_3 + 1):
                if(board[q][w]  == num):
                    return False
    return True

# removeNumber() removes a number from the board
#
# Input:  board; the 2d list of values,
#         row; the integer row to remove from, 
#         col; the integer column to remove from
# Output: board; returns the 2d list updated board
def removeNumber(board, row, col):
    board[row][col] = 0
    return board

# checkCorrectness() compares the suggested number to the solution
# 
# Input:  row; the suggested integer row,
#         col; the suggested integer column,
#         num; the integer to check,
#         solution; the solution 2d list to compare to
# Output: correct; a boolean that declares whether the suggested
#         value is right or not
def checkCorrectness(solution, num, row, col):
    if(solution[row][col] == num):
        return True
    else:
        return False

# createDeepCopy() creates a deep copy of a 2d list
# 
# Input:  list2d; the 2d list that will be made into a deep copy
# Output: deepList; the newly created 2d list deep copy
def createDeepCopy(list2d):
    deepList = []
    for i in range(0, len(list2d)):
        deepList.append(list(list2d[i]))
    return deepList

# checkIfProgramEnd() ends program when correctness checking is
#                     off and the puzzle matches the solution.
# Input:  board; the user's 2d list, solution; the  2d list
#         solution to compare the board to.
# Output: exitflag; the boolean flag that will end the program.
def checkIfProgramEnd(board, solution, exitFlag):
    exitFlag = True 
    for y in range(0, len(board)):
        for t in range(0, len(board[y])):
            if(board[y][t] != solution[y][t]):
                exitFlag = False
    return exitFlag
    
def main():
    fileName = input("Enter the filename of the Sudoku Puzzle: ")
    board = readFile(fileName)
    # Casts each of the individual values of the list as integers
    board = castInt(board)
    boardValues = [[(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],
                   [(),(),(),(),(),(),(),(),()],]

    prettyPrint(board)
    decision = input("play (p) or solve (s)? ")
    while(decision != PLAY and decision != SOLVE):
        print("please enter a 'p' or an 's'.")
        decision = input("play (p) or solve (s)? ")
    #if the player decides to solve the puzzle
    if(decision == SOLVE):
        solve(board, 0, 0, boardValues)
        print("Solved board: ")
        prettyPrint(board)
    #if the player decides to play the game
    elif(decision == PLAY):
        correctCheck = input("correctness checking? (y/n) ")
        while(correctCheck != YES and correctCheck != NO):
            print("Try typing a 'y' or a 'n' this time")
            correctCheck = input("correctness checking? (y/n) ")

        #if correctness checking is on
        if(correctCheck == YES):
            moveList = []
            solution = readFile(fileName)
            # Casts each of the individual values of the list as integers
            solution = castInt(solution)
            solve(solution, 0, 0, boardValues)
            exitFlag = False
            while(exitFlag != True):
                choice = input("play number (p), save(s), undo (u), quit (q): ") 
                while(choice != PLAY and choice != SAVE and
                      choice != UNDO and choice != QUIT):
                    print("please choose one of the correct options")
                    print("play number (p),", end = "")
                    choice = input(" save(s), undo (u), quit (q): ")
                
                if(choice == PLAY):
                    row = int(input("Enter a row number (1-9): "))
                    col = int(input("Enter a column number (1-9): "))
                    row -= 1
                    col -= 1
                    #checks if the cell is already occupied
                    while(board[row][col] != 0):
                        print("This cell has a number in it. Try again")
                        row = int(input("Enter a row number (1-9): "))
                        col = int(input("Enter a column number (1-9): "))
                        row -= 1
                        col -= 1
                    print("Enter a number to put in cell (" + str(row + 1)\
                          + ", " + str(col + 1) + ")", end = "")
                    num = int(input(": "))
                    validNum = validateNumber(board, num, row, col)
                    while(validNum == False):
                        print("Not a valid number, try again")
                        row = int(input("Enter a row number (1-9): "))
                        col = int(input("Enter a column number (1-9): "))
                        row -= 1
                        col -= 1
                        #checks if the cell is already occupied
                        while(board[row][col] != 0):
                            print("This cell already has a number in it."\
                                  "Try again")
                            row = int(input("Enter a row number (1-9): "))
                            col = int(input("Enter a column number (1-9): "))
                            row -= 1
                            col -= 1
                        print("Enter a number to put in cell (" + str(row + 1)\
                              + ", " + str(col + 1) + ")", end = "")
                        num = int(input(": "))
                        validNum = validateNumber(board, num, row, col)
                    #correctness section
                    correctness = checkCorrectness(solution, num, row, col)
                    while(correctness == False):
                        print("That number is not correct")
                        print("Try again")
                        row = int(input("Enter a row number (1-9): "))
                        col = int(input("Enter a column number (1-9): "))
                        row -= 1
                        col -= 1
                        #checks if the cell is already occupied
                        while(board[row][col] != 0):
                            print("This cell already has a number", end = "")
                            print("in it. Try again")
                            row = int(input("Enter a row number (1-9): "))
                            col = int(input("Enter a column number (1-9): "))
                            row -= 1
                            col -= 1
                        print("Enter a number to put in cell (" + str(row + 1)\
                              + ", " + str(col + 1) + ")", end = "")
                        num = int(input(": "))
                        validNum = validateNumber(board, num, row, col)
                        while(validNum == False):
                            print("Not a valid number, try again")
                            row = int(input("Enter a row number (1-9): "))
                            col = int(input("Enter a column number (1-9): "))
                            row -= 1
                            col -= 1
                            #checks if the cell is already occupied
                            while(board[row][col] != 0):
                                print("This cell already has a ", end = "")
                                print("number in it. Try again")
                                row = int(input("Enter a row (1-9): "))
                                col = int(input("Enter a column (1-9): "))
                                row -= 1
                                col -= 1
                            print("Enter a number to put in cell (" + str(row + 1)\
                                  + ", " + str(col + 1) + ")", end = "")
                            num = int(input(": "))
                            validNum = validateNumber(board, num, row, col)
                        correctness = checkCorrectness(solution, num, row, col)
                    #end correctness section
                    board[row][col] = num
                    moveList.append([row, col, num])
                    print("Updated board:")
                    prettyPrint(board)
                    
                elif(choice == SAVE):
                    print("What would you like ", end = "")
                    saveFileName = input("the file name to be? ")
                    savePuzzle(board, saveFileName)
                elif(choice == UNDO):
                    if(len(moveList) == 0):
                        print("There is nothing to undo")
                    else:
                        print("removing number", moveList[len(moveList) - 1]\
                              [DEEP_COPY_CONSTANT], "from (", end = "")
                        print(moveList[len(moveList) - 1][0], end = "")
                        print(",", moveList[len(moveList) - 1][1], end = "")
                        print(")")
                        board = removeNumber(board,
                                             moveList[len(moveList) - 1][0],
                                             moveList[len(moveList) - 1][1])
                        
                        moveList = moveList[:len(moveList) - 1]
                        print("Updated board:")
                        prettyPrint(board)
                        
                elif(choice == QUIT):
                    exitFlag = True

                if(choice != QUIT):
                    exitFlag = checkIfProgramEnd(board, solution, exitFlag)
                    
        #if correctness checking is off
        elif(correctCheck == NO):
            moveList = []
            solution = readFile(fileName)
            # Casts each of the individual values of the list as integers
            solution = castInt(solution)
            solve(solution, 0, 0, boardValues)
            
            exitFlag = False
            while(exitFlag != True):
                choice = input("play number (p), save(s), undo (u), quit (q): ") 
                while(choice != PLAY and choice != SAVE and
                      choice != UNDO and choice != QUIT):
                    print("please choose one of the correct options")
                    print("play number (p),", end = "")
                    choice = input(" save(s), undo (u), quit (q): ")
                
                if(choice == PLAY):
                    row = int(input("Enter a row number (1-9): "))
                    col = int(input("Enter a column number (1-9): "))
                    row -= 1
                    col -= 1
                    #checks if the cell is already occupied
                    while(board[row][col] != 0):
                        print("This cell has a number in it. Try again")
                        row = int(input("Enter a row number (1-9): "))
                        col = int(input("Enter a column number (1-9): "))
                        row -= 1
                        col -= 1
                    print("Enter a number to put in cell (" + str(row + 1)\
                          + ", " + str(col + 1) + ")", end = "")
                    num = int(input(": "))
                    validNum = validateNumber(board, num, row, col)
                    while(validNum == False):
                        print("Not a valid number, try again")
                        row = int(input("Enter a row number (1-9): "))
                        col = int(input("Enter a column number (1-9): "))
                        row -= 1
                        col -= 1
                        #checks if the cell is already occupied
                        while(board[row][col] != 0):
                            print("This cell already has a number in it."\
                                  "Try again")
                            row = int(input("Enter a row number (1-9): "))
                            col = int(input("Enter a column number (1-9): "))
                            row -= 1
                            col -= 1
                        print("Enter a number to put in cell (" + str(row + 1)\
                              + ", " + str(col + 1) + ")", end = "")
                        num = int(input(": "))
                        validNum = validateNumber(board, num, row, col)
                    
                    board[row][col] = num
                    moveList.append([row, col, num])
                    print("Updated board:")
                    prettyPrint(board)
                    
                elif(choice == SAVE):
                    print("What would you like ", end = "")
                    saveFileName = input("the file name to be? ")
                    savePuzzle(board, saveFileName)
                elif(choice == UNDO):
                    if(len(moveList) == 0):
                        print("There is nothing to undo")
                    else:
                        print("Removing number", moveList[len(moveList) - 1]\
                              [DEEP_COPY_CONSTANT], "from (", end = "")
                        print(moveList[len(moveList) - 1][0] + 1, end = "")
                        print(",", moveList[len(moveList) - 1][1] + 1, end = "")
                        print(")")
                        board = removeNumber(board,
                                             moveList[len(moveList) - 1][0],
                                             moveList[len(moveList) - 1][1])
                        moveList = moveList[:len(moveList) - 1]
                        print("Updated board:")
                        prettyPrint(board)
                        
                elif(choice == QUIT):
                    exitFlag = True

                if(choice != QUIT):
                    exitFlag = checkIfProgramEnd(board, solution, exitFlag)
        print("Good bye! Here is the final board:")
        prettyPrint(board)
main()
