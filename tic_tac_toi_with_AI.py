import os
import time

# display board
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_', ]

# If game is still going
game_still_going = True

# Who won? or Tie
winner = None

# Whose turn is it
global current_player
global player_1
global player_2


# Method for display board
def display_board():
    print(' ' + board[0] + '|' + board[1] + '|' + board[2])
    print(' ' + board[3] + '|' + board[4] + '|' + board[5])
    print(' ' + board[6] + '|' + board[7] + '|' + board[8])


# Play Tic Tac Toe game
def play_game():

    select_symbol = input("Choose 'X' or 'O' : ")

    if select_symbol == 'X' or select_symbol == 'O':
        global current_player
        current_player = select_symbol

        print('You are : ' + select_symbol)
        # print(current_player)
        #select_player()
        # Display initial board
        display_board()

        # While the game is still going
        while game_still_going:
            # handle a single turn of an arbitrary player
            handle_turn(current_player)

            # Check if game is over or not
            check_if_game_over()

            # Flip player
            flip_player()

            # The game has ended
        if winner == "X" or winner == "O":
            print(winner + ': wins')
            time.sleep(3)
        else:
            print("This is a Tie.")
            time.sleep(3)
    else:
        print('You enter wrong symbol please start again.')


def handle_turn(player):
    print(player + "'s turn.")
    position = input('Choose a position from 1-9.')

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Invalid position. Please select a valid from 1-9 : ')
        position = int(position) - 1

        if board[position] == '_':
            valid = True
        else:
            print("You can't put here go to other part")
    board[position] = player
    #os.system('cls')
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Setting global winner
    global winner

    # Check row
    row_winner = check_row()
    # Check column
    column_winner = check_column()
    # Check diagonal
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner

    return winner


def check_row():
    # Setting up global variable
    global game_still_going

    # Check if any of the row has same value or not
    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'

    # If any row has match flag that there is win
    if row_1 or row_2 or row_3:
        game_still_going = False

        # Return the winner X or O
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]

    return


def check_column():
    # Setting up global variable
    global game_still_going
    # Check if any of the column has same value or not
    column_1 = board[0] == board[3] == board[6] != '_'
    column_2 = board[1] == board[4] == board[7] != '_'
    column_3 = board[2] == board[5] == board[8] != '_'

    # If any cloumn has match flag that there is win
    if column_1 or column_2 or column_3:
        game_still_going = False

        # Return the winner X or O
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]

    return


def check_diagonal():
    # Setting up global variable
    global game_still_going

    # Check if any diagonal has same value or not
    diagonal_1 = board[0] == board[4] == board[8] != '_'
    diagonal_2 = board[2] == board[4] == board[6] != '_'

    # If any diagonal has match flag that there is win
    if diagonal_1 or diagonal_2:
        game_still_going = False
        # Return the winner X or O
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[2]

    return


def check_if_tie():
    # Setting up global variable
    global game_still_going

    if '_' not in board:
        game_still_going = False

    return
#//////////////////////////////////////////////////////////////////////////////
#
# def flip_player():
#     global player_1
#     global player_2
#
#     if player_1 == 'X':
#         print('Player 1 : ' + player_1)
#         player_2 = 'O'
#         print('Player 2 : ' + player_2)
#
#     elif player_1 == 'O':
#         print('Player 1 : ' + player_1)
#         player_2 = 'X'
#         print('Player 2 : ' + player_2)
#
#     elif player_2 == 'X':
#         print('Player 2 : ' + player_2)
#         player_1 = 'O'
#         print('Player 2 : ' + player_1)
#
#     elif player_2 == 'O':
#         print('Player 2 : ' + player_2)
#         player_1 = 'X'
#         print('Player 2 : ' + player_1)
#
#
# def select_player():
#     valid = False
#     global player_1
#     global player_2
#     choose_player = input("Choose 'X' or 'O' : ")
#     while not valid:
#         while choose_player not in ['X', 'O']:
#             choose_player = input('Wrong input please select right symbol : ')
#
#         if choose_player == 'X' or choose_player == 'O':
#             player_1 = choose_player
#             #print('Player 1 : ' + player_1)
#             valid = True
#         else:
#             print('Error occurs.')

#////////////////////////////////////////////////////////////////////////////////////


def flip_player():
    # Setting up global variable
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

    return


def select_player():
    # Setting up global variable
    global current_player
    global player_1
    global player_2

    select_symbol = input("Choose 'X' or 'O' : ")

    if select_symbol == 'X' or select_symbol == 'O':
        global current_player
        current_player = select_symbol
        global player_1
        player_1 = current_player

        # Current player
        print('You are : ' + select_symbol)
    elif player_1 == 'X' or player_1 == 'O':
        global player_2
        player_2 = player_1

    else:
        print('You entered a wrong symbol please start again thank you')


play_game()

# def continue_game():
#     play_game()
#
#     while check_if_game_over():
#         play_game()
#
#
# if __name__ == '__main__':
#     continue_game()
































