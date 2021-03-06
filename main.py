
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
game_over = False


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



def make_move(row,col):
    # global game_game board
    global game_board
    # get player turn and store as variable 'move'
    move = get_turn()
    # change game_board[row][col] = 'move'
    game_board[int(row)][int(col)] = move
    # change player turn
    change_turn()



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
    >>> is_valid_move('x',2323)
    False
    >>> is_valid_move(-1,3)
    False

    '''



    global game_board

    if str(row).isdigit() == False or str(col).isdigit() == False:

        return False


    elif (int(row) < 0 or int(row) > 2) or (int(col) < 0 or int(col) > 2):
        return False

    elif game_board[int(row)][int(col)] != "*":
        return False

    else:
        return True



'''
USAGE: Ask the user for a row and a column
INPUT: NONE
OUTPUT: The row and column
'''
def get_user_move():

    row = input("Enter a row between 0 and 2 >>> ")

    col = input("Enter a column between 0 and 2 >>> ")

    if is_valid_move(row,col) == True:


        make_move(row,col)
        display_board()
    else:

        get_user_move()






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

'''
USAGE: Checks if the board is filled
INPUT: NONE
GLOBAL: game_board, game_over
OUTPUT: TRUE if full, False OTHERWISE
'''
def is_board_filled():
    '''
    >>> global game_board
    >>> create_board()
    >>> is_board_filled()
    False
    >>> fill_board()
    >>> is_board_filled()
    True


    '''

    # Get global game_board, game_over
    global game_board

    # Loop over rows
    for i in range(0,3):
        #Loop over columns
        for j in range(0,3):
            spot = game_board[i][j]
            # spot = current spot on board
            if spot == "*":
            # Check if spot is equal to '*'
                return False
                # return False
    return True
    # return True


'''
USAGE: Creating a filled board to check is_board_filled function
INPUT: NONE
GLOBAL: game_board
OUTPUT: NONE
'''
def fill_board():

    # global game_board
    global game_board
    # loop over rows 0 to 3
    for i in range(0, 3):
        # loop over columns 0 to 3
        for j in range(0, 3):
            # set game_board[i][j] = 'X'
            game_board[i][j] = 'X'

'''
USAGE:
INPUT:
GLOBAL:
OUTPUT:
'''
def clear_board():
    global game_board

    # global game_board
    global game_board
    # loop over rows 0 to 3
    for i in range(0, 3):
        # loop over columns 0 to 3
        for j in range(0, 3):
            # set game_board[i][j] = 'X'
            game_board[i][j] = '*'


def is_horizontal_win():
    '''
    >>> global game_board
    >>> create_board()
    >>> game_board[0][0] = game_board[0][1] = game_board[0][2]  = 'X'

    >>> is_horizontal_win()
    True

    >>> clear_board()

    >>> game_board[1][0] = game_board[1][1] = game_board[1][2]  = 'O'

    >>> is_horizontal_win()
    True

    >>> clear_board()

    >>> game_board[1][0] = game_board[1][1]  = 'O'
    >>> game_board[1][2] = 'X'

    >>> is_horizontal_win()
    False


    '''
    global game_board

    # [
    #
    # [X, O, X] --> list1
    #
    # [O, O, X] --> list2
    #
    # [X, O, X] --> list3 --> This will win
    #
    #  Values row takes on --> 0, 1, 2
    #
    # ]



    for row in game_board:

        if row[0] == row[1] == row[2] == 'X':
            return True

        elif row[0] == row[1] == row[2] == 'O':
            return True
    return False





def is_vertical_win():
    '''
     >>> global game_board
     >>> create_board()
     >>> game_board[0][0] = game_board[1][0] = game_board[2][0]  = 'X'

     >>> is_vertical_win()
     True

     >>> clear_board()

     >>> game_board[0][0] = game_board[1][0] = game_board[2][0]  = 'O'

     >>> is_vertical_win()
     True

     >>> clear_board()

     >>> game_board[1][0] = game_board[1][1]  = 'O'
     >>> game_board[1][2] = 'X'

     >>> is_vertical_win()
     False


     '''

    pass

'''
CHECKS IF THE BOARD HAS A FORWARD DIAGONAL WIN EXAMPLE BELOW

        - - X
        - X -
        X - -

'''
def is_forward_diagonal_win():
    '''
     >>> global game_board
     >>> create_board()
     >>> game_board[0][2] = game_board[1][1] = game_board[2][0]  = 'X'

     >>> is_forward_diagonal_win()
     True

     >>> clear_board()

     >>> game_board[0][0] = game_board[1][1] = game_board[2][0]  = 'X'
     >>> is_forward_diagonal_win()
     False

    '''

    pass



'''
CHECKS IF THE BOARD HAS A BACKWARD DIAGONAL WIN EXAMPLE BELOW

        X - -
        - X -
        - - X

'''
def is_backward_diagonal_win():

    '''
     >>> global game_board
     >>> create_board()
     >>> game_board[0][0] = game_board[1][1] = game_board[2][2]  = 'X'

     >>> is_backward_diagonal_win()
     True

     >>> clear_board()

     >>> game_board[0][0] = game_board[1][1] = game_board[2][0]  = 'X'
     >>> is_backward_diagonal_win()
     False

    '''
    pass



def is_diagonal_win():
    '''
     >>> global game_board
     >>> create_board()
     >>> game_board[0][0] = game_board[1][1] = game_board[2][2]  = 'X'

     >>> is_diagonal_win()
     True

     >>> clear_board()

     >>> game_board[2][0] = game_board[1][1] = game_board[0][2]  = 'O'

     >>> is_diagonal_win()
     True

     >>> clear_board()

     >>> game_board[0][0] = game_board[1][1]  = 'O'
     >>> game_board[2][2] = 'X'

     >>> is_diagonal_win()
     False


    '''
    global game_board
    if is_forward_diagonal_win() or is_backward_diagonal_win():
        return True
    else:
        return False



'''
USAGE: Checks if either of our 3 win conditons are met
GLOBALS: game_board
INPUT: None --> Uses global variables...See above
OUTPUT: returns True if any win condition is met, False otherwise
'''
def is_win():
    '''
     >>> global game_board
     >>> create_board()
     >>> game_board[0][0] = game_board[1][1] = game_board[2][2]  = 'X'

     >>> is_win()
     True

     >>> clear_board()

     >>> game_board[0][0] = game_board[1][0] = game_board[2][0]  = 'X'

     >>> is_win()
     True

     >>> clear_board()

     >>> game_board[0][0] = game_board[0][1] = game_board[0][2]  = 'X'

     >>> is_win()
     True

     >>> clear_board()

     >>> game_board[0][0] = game_board[0][1] = game_board[1][2] = game_board[2][0] = game_board[2][1]   = 'X'
     >>> game_board[0][2] = game_board[1][0] = game_board[1][1] = game_board[2][2] = 'O'

     >>> is_win()
     False




    '''

    pass




# def main():
#
#     global game_over
#     create_board()
#     display_board()
#
#
#
#
#
#
#
#
#
#     while is_board_filled() == False:
#         get_user_move()

#
#
#
# main()





if __name__ == '__main__':
    import doctest

    #doctest.run_docstring_examples(is_horizontal_win, globals())

    # UNCOMMENT TO RUN IS THE DOC-TEST FOR VERITCAL WIN CONDITIONS
    #doctest.run_docstring_examples(is_vertical_win, globals())

    # UNCOMMENT TO RUN IS THE DOC-TEST FOR is_backward_diagonal_win
    #doctest.run_docstring_examples(is_backward_diagonal_win, globals())

    # UNCOMMENT TO RUN IS THE DOC-TEST FOR is_forward_diagonal_win
    #doctest.run_docstring_examples(is_forward_diagonal_win, globals())

    # UNCOMMENT TO RUN IS THE DOC-TEST FOR DIAGONAL WIN CONDITIONS
    # doctest.run_docstring_examples(is_diagonal_win, globals())

    # UNCOMMENT TO RUN IS THE DOC-TEST FOR is_win() function
    # doctest.run_docstring_examples(is_win, globals())
