'''TIC TAC TOE by Troy Hans
   A single player tic-tac-toe console game'''

from random import randint
from os import system
from time import sleep

BOARD = ['']+[str(x) for x in range(1, 10)]
PLAYER = 'X'
COMPUTER = 'O'
CURRENT_PLAYER = PLAYER

def game():
    '''running the game'''
    while True:
        player_select()
        if check_for_win_or_tie():
            break
        computer_select()
        if check_for_win_or_tie():
            break

def display_board():
    '''clears the screen and displays the game board'''
    global BOARD
    system('clear')
    print('\t TIC TAC TOE')
    print('\t-------------')
    print(f'\t| {BOARD[7]} | {BOARD[8]} | {BOARD[9]} |')
    print('\t-------------')
    print(f'\t| {BOARD[4]} | {BOARD[5]} | {BOARD[6]} |')
    print('\t-------------')
    print(f'\t| {BOARD[1]} | {BOARD[2]} | {BOARD[3]} |')
    print('\t-------------')
    print('\n')

def player_select():
    '''The player inputs a square selection'''
    global BOARD
    global CURRENT_PLAYER
    CURRENT_PLAYER = PLAYER
    while True:
        try:
            display_board()
            user_input = int(input("\t   Player\nPlease choose a square 1 - 9: "))
            if user_input in range(1, 10) and BOARD[user_input].isdigit():
                BOARD[user_input] = PLAYER
                break
            print('You must select an unplayed square')
            sleep(2)
        except ValueError:
            continue

def computer_select():
    '''The computer dumb selects a random available square'''
    global BOARD
    global CURRENT_PLAYER
    CURRENT_PLAYER = COMPUTER
    display_board()
    print('   The Computer is playing')
    sleep(randint(2, 5))
    while True:
        comp_choice = randint(1, 9)
        if BOARD[comp_choice].isdigit():
            BOARD[comp_choice] = COMPUTER
            display_board()
            print(f'   I have chosen square #{comp_choice}')
            sleep(2)
            break

def check_for_win_or_tie():
    '''Checks for a win or tie'''
    global BOARD
    global CURRENT_PLAYER
    display_board()
    if (BOARD[1] == BOARD[2] == BOARD[3] or
        BOARD[4] == BOARD[5] == BOARD[6] or
        BOARD[7] == BOARD[8] == BOARD[9] or
        BOARD[1] == BOARD[4] == BOARD[7] or
        BOARD[2] == BOARD[5] == BOARD[8] or
        BOARD[3] == BOARD[6] == BOARD[9] or
        BOARD[1] == BOARD[5] == BOARD[9] or
        BOARD[3] == BOARD[5] == BOARD[7]):
        print(f'\t   {CURRENT_PLAYER} WINS!')
        return True
    if ''.join(BOARD[1:]).isalpha():
        print('\tThe game is a Tie')
        return True
    
    return False

if __name__ == '__main__':
    game()
    