import pyttsx3
import random as rn
import os

# Global variable rock, paper and scissor

global rock
global paper
global scissor
global program
global game_running

random_choose = ['ROCK', 'PAPER', 'SCISSOR']

global player1
global player2


def winner():

    # Rock
    if player1 == rock and player2 == paper:
        print(player2 + ' wins')

    elif player1 == rock and player2 == scissor:
        print(player1 + ' wins')

    elif player1 == rock and player2 == rock:
        print('This is tie.')

    # Paper
    elif player1 == paper and player2 == scissor:
        print(player2 + ' wins')

    elif player1 == paper and player2 == rock:
        print(player1 + ' wins')

    elif player1 == paper and player2 == paper:
        print('This is tie.')

    # Scissor
    elif player1 == scissor and player2 == rock:
        print(player2 + ' wins')

    elif player1 == scissor and player2 == paper:
        print(player1 + ' wins')

    elif player1 == scissor and player2 == scissor:
        print('This is tie.')


def game_input():

    # Global variables setting
    global rock
    global paper
    global scissor
    global program
    global player1
    global player2

    valid = True
    print("Press R/r for Rock  \nPress P/p for Paper  \nPress S/s for Scissor  ")
    choose = input("Enter your choice : ")

    while valid:

        if choose == 'R' or choose == 'r':
            rock = 'ROCK'
            paper = 'PAPER'
            scissor = 'SCISSOR'
            program = rn.randint(0, (len(random_choose) - 1))
            player1 = rock
            player2 = random_choose[program]
            print('*****  ' + player1 + '  ' + 'V/S' + '  ' + player2 + '  *****')
            winner()
            valid = False

        elif choose == 'P' or choose == 'p':
            rock = 'ROCK'
            paper = 'PAPER'
            scissor = 'SCISSOR'
            program = rn.randint(0, (len(random_choose) - 1))
            player1 = paper
            player2 = random_choose[program]
            print('*****  ' + player1 + '  ' + 'V/S' + '  ' + player2 + '  *****')
            winner()
            valid = False

        elif choose == 'S' or choose == 's':
            rock = 'ROCK'
            paper = 'PAPER'
            scissor = 'SCISSOR'
            program = rn.randint(0, (len(random_choose) - 1))
            player1 = scissor
            player2 = random_choose[program]
            print('*****  ' + player1 + '  ' + 'V/S' + '  ' + player2 + '  *****')
            winner()
            valid = False

        else:
            print("Please choose right alphabet.")
            valid = False


def play():

    global game_running

    game_running = True

    while game_running:
        game_input()

        continue_ = input("Press Y/y for continue : ")

        if continue_ == 'Y' or continue_ == 'y':
            game_running = True
            os.system('cls')
        else:
            game_running = False


play()








































































































































































