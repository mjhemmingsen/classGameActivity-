
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
player_turn = 0 # X --> 0 and O--> 1

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
USAGE: Checks if the users move is valid or not
INPUT: A row and a col integer
OUTPUT: True if valid False otherwise
'''
def is_valid_move(row, col):
    '''
    >>> global game_board
    >>> create_board()
    >>> is_valid_move(0,0)
    True
    >>> game_board[2][2] = 'X'
    >>> is_valid_move(2,2)
    False

    '''

    # global variable game_board

    # Check if  row or column is not a digit
        # return false

    #elif check if row and col are not between 0 and 2

        # return false

    # elif check if game_board[row][col] is not equal to '*':

        # return false

    # else

        # return true

'''
USAGE:
INPUT:
OUTPUT:
'''
def get_user_move():
    # TODO implement this method
    pass

'''
USAGE: Get the current players move
INPUT: NONE use player_turn global variable
OUTPUT: return either x or o
'''
def get_turn():
    '''
    >>> global player_turn
    >>> get_turn()
    'X'

    '''

    global player_turn


    if player_turn == 0:
        return "X"
    else:
        return "O"





'''
USAGE: Change from player 1 to player 2 with each turn
INPUT: None - use global variable player_turn
OUTPUT: None
'''
def change_turn():

    global player_turn

    if player_turn == 0:
        player_turn = 1
    elif player_turn == 1:
        player_turn = 0
    else:
        print("error")



def main():

    global game_board

    create_board()

    display_board()

    get_turn()


    print(player_turn)

    change_turn()

    print(player_turn)

    change_turn()

    print(player_turn)

main()



if __name__ == '__main__':
    import doctest

    doctest.run_docstring_examples(change_turn, globals())

