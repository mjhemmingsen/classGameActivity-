
'''

USER REQUIREMENTS (Unordered)

-> There needs to be a 3 x 3 board

-> Need user input for player 1 and player 2

-> Need to be able to make move by choosing spot on board

-> Announce a winner

-> Check for a winner

-> display current board to the user

'''

'''
USER REQUIREMENTS (PRIORITY)

PRIORITY LEVEL 1

    -> There needs to be a 3 x 3 board (DONE-TESTED)
    -> display current board to the user (DONE-TESTED)

PRIORITY LEVEL 2


    -> Need to be able to make move by choosing spot on board
        // users need to input two numbers in order to make a move
        // numbers must be between 0 and 2
        // keep track of users input
        // if spot is in use ask again

PRIORITY LEVEL 3

    -> Check for a winner
    -> Announce a winner

'''

game_board = []
player_turn = 0

'''
USAGE: Creates a 3 x 3 board that will store our values in a
2d array in our global variable game_board that will be represented by the following

*  *  *
*  *  *
*  *  *

INPUT: NONE

OUTPUT: NONE

'''
def create_board():
    global game_board

    for i in range(0,3):
        temp_list = []

        for j in range(0,3):

            temp_list.append('*')

        game_board.append(temp_list)



'''
USUAGE: displays the current state of the game board

*  *  *
*  *  *
*  *  *

INPUT: NONE

OUTPUT: print our board
'''
def display_board():
    global game_board
    our_board = '''
                {} {} {}

                {} {} {}

                {} {} {}
                '''.format(game_board[0][0], game_board[0][1], game_board[0][2], game_board[1][0], game_board[1][1], game_board[1][2], game_board[2][0], game_board[2][1], game_board[2][2])

    print(our_board)



'''
USAGE:
INPUT:
OUTPUT:
'''
def make_move():
    # TODO implement this method
    pass

'''
USAGE:
INPUT:
OUTPUT:
'''
def is_valid_move():
    # TODO implement this method
    pass

'''
USAGE:
INPUT:
OUTPUT:
'''
def get_user_move():
    # TODO implement this method
    pass

'''
USAGE:
INPUT:
OUTPUT:
'''
def get_turn():
    # TODO implement this method
    pass


def main():

    global game_board

    create_board()

    display_board()

main()

