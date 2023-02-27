'''TIC TAC TOE by Troy Hans
   A single player tic-tac-toe console game'''

from random import randint
from os import system
from time import sleep

board = ['']+[str(x) for x in range(1, 10)]
player = 'X'
computer = 'O'
current_player = player

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
    system('clear')
    print('\t TIC TAC TOE')
    print('\t-------------')
    print(f'\t| {board[7]} | {board[8]} | {board[9]} |')
    print('\t-------------')
    print(f'\t| {board[4]} | {board[5]} | {board[6]} |')
    print('\t-------------')
    print(f'\t| {board[1]} | {board[2]} | {board[3]} |')
    print('\t-------------')
    print('\n')

def player_select():
    '''The player inputs a square selection'''
    current_player = player
    while True:
        try:
            display_board()
            user_input = int(input("\t   player\nPlease choose a square 1 - 9: "))
            if user_input in range(1, 10) and board[user_input].isdigit():
                board[user_input] = player
                break
            print('You must select an unplayed square')
            sleep(2)
        except ValueError:
            continue

def computer_select():
    '''The computer dumb selects a random available square'''
    current_player = computer
    display_board()
    print('   The computer is playing')
    sleep(randint(2, 5))
    while True:
        comp_choice = randint(1, 9)
        if board[comp_choice].isdigit():
            board[comp_choice] = computer
            display_board()
            print(f'   I have chosen square #{comp_choice}')
            sleep(2)
            break

def check_for_win_or_tie():
    '''Checks for a win or tie'''
    display_board()
    if (board[1] == board[2] == board[3] or
        board[4] == board[5] == board[6] or
        board[7] == board[8] == board[9] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[3] == board[6] == board[9] or
        board[1] == board[5] == board[9] or
        board[3] == board[5] == board[7]):
        print(f'\t   {current_player} WINS!')
        return True
    if ''.join(board[1:]).isalpha():
        print('\tThe game is a Tie')
        return True
    
    return False

if __name__ == '__main__':
    game()
    