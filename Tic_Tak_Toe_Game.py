#import os

#-----Global veriable-----

#Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
#If game is still going

game_still_going = True

#Who won? or tie
winner = None

#Whose turn is it

current_player = "X"

#####Display board
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
#####Display board

# Play a game of Tic Tak Toe

def play_game():
    #Display initial board
    display_board()

   #While the game is still going
    while game_still_going:

     #Handle a single turn of an arbitrary player
        handle_turn(current_player)

      #Check if the game has ended
        check_if_game_over()

      #Flip to the other player
        flip_player()

# The game has ended

    if winner == "X" or winner == "O":
        print(winner +" won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):

    print(player+"'s turn.")
    position = input("Choose a position from 1-9 : ")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input.Choose a position from 1-9.")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't write here go to other part.")

    board[position] = player
    display_board()
#    os.system("cls")

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #Setting global veriable
    global winner

    #Check rows
    row_winner = check_rows()
    #Check columns
    column_winner = check_columns()
    #Check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return

def check_rows():
    #set up global veriable
    global game_still_going
 # Check if any of the row have same value(and  is not same)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
  #If any row does have a match,flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
  #Return the winner (X or O)
    if row_1:
      #  print("X wins")
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return

def check_columns():
    # set up global veriable
    global game_still_going
    # Check if any of the column have same value(and  is not same)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match,flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return

def check_diagonals():
    # set up global veriable
    global game_still_going
    # Check if any of the diagonals have same value(and  is not same)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonals does have a match,flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]

    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return

def flip_player():

#Set global veriable
    global current_player
# If the current player is X ,then change it to O
    if current_player == "X":
        current_player = "O"
# If the current player is O , then change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()



