#S309499 Deniz Guler Tic Tac Toe project


playboard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

boarddisplay=[[" 1 ", " 2 ", " 3 "],
              [" 4 ", " 5 ", " 6 "],
              [" 7 ", " 8 ", " 9 "]]

board_keys = []

for i in playboard:
    board_keys.append(i)

def printBoard(board):
    print("The numbers of the squares are shown as below.")
    print("\n")
    print(boarddisplay[0])
    print(boarddisplay[1])
    print(boarddisplay[2])
    print("\n")

    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    turn ='X'
    count = 0

    for n in range(10):
        printBoard(playboard)
        print("It's your turn "+ turn +". Where would you like to put your mark in?:")

        mark = input()

        if playboard[mark] == ' ':
            playboard[mark] =turn
            count += 1
        else:
            print("That square is already filled. Please choose another one.")


#winner
        if count>= 5:
            if playboard['1']== playboard['2']== playboard['3'] != '' or playboard['4']== playboard['5']== playboard['6']!='' or playboard['7']== playboard['8']== playboard['9'] != '' or playboard['1']== playboard['4']== playboard['7'] != '' or playboard['2']== playboard['5']== playboard['8'] != '' or playboard['3']== playboard['6']== playboard['9'] != '' :
                printBoard(playboard)
                print("Game Over.")
                print("\n")
                print(turn + " has won.")
                break


        #tie
        if count == 9:
            print("Game Over.")
            print("\n")
            print("It's a tie.")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'




game()






