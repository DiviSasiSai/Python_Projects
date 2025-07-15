theBoard = {'top-l':" ",'top-m':" ","top-r":" ",
            'mid-l':" ",'mid-m':" ","mid-r":" ",
            'lower-l':" ",'lower-m':" ","lower-r":" "}

def printBoard(board):
    print(board['top-l']+"|"+board['top-m']+"|"+board['top-r'])
    print("-+-+-")
    print(board['mid-l']+"|"+board['mid-m']+"|"+board['mid-r'])
    print("-+-+-")
    print(board['lower-l']+"|"+board['lower-m']+"|"+board['lower-r'])

turn = "X"

for i in range(9):
    printBoard(theBoard)
    move = input(f"Turn {turn} Enter your move: ")
    theBoard[move] = turn
    if ((theBoard['top-l'] == "X" and theBoard['top-m'] == "X" and theBoard['top-r'] == "X") or
        (theBoard['mid-l'] == "X" and theBoard['mid-m'] == "X" and theBoard['mid-r'] == "X") or
        (theBoard['lower-l'] == "X" and theBoard['lower-m'] == "X" and theBoard['lower-r'] == "X") or
        (theBoard['top-l'] == "X" and theBoard['mid-m'] == "X" and theBoard['lower-r'] == "X") or
        (theBoard['top-r'] == "X" and theBoard['mid-m'] == "X" and theBoard['lower-l'] == "X") or
        (theBoard['top-r'] == "X" and theBoard['mid-r'] == "X" and theBoard['lower-r'] == "X") or
        (theBoard['top-l'] == "X" and theBoard['mid-l'] == "X" and theBoard['lower-l'] == "X")):
        print("X was Win....")
        printBoard(theBoard)
        break
    if ((theBoard['top-l'] == "O" and theBoard['top-m'] =="O" and theBoard['top-r'] == "O") or
        (theBoard['mid-l'] == "O" and theBoard['mid-m'] == "O" and theBoard['mid-r'] == "O") or
        (theBoard['lower-l'] == "O"and theBoard['lower-m'] == "O" and theBoard['lower-r'] == "O") or
        (theBoard['top-l'] == "O" and theBoard['mid-m'] == "O" and theBoard['lower-r'] == "O") or
        (theBoard['top-r'] == "O" and theBoard['mid-m'] == "O" and theBoard['lower-l'] == "O") or
        (theBoard['top-r'] == "O" and theBoard['mid-r'] == "O"and theBoard['lower-r'] == "O") or
        (theBoard['top-l'] == "O" and theBoard['mid-l'] == "O" and theBoard['lower-l'] == "O")):
        print("O was Win....")
        printBoard(theBoard)
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
else:
    print("Match was Tie")