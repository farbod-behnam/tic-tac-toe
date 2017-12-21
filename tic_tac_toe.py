from __future__ import print_function
import sys

# -----------------------------------------------------------------------------------
# player_input
# -----------------------------------------------------------------------------------

def display_board(cell_list):
    """
    display_board: display a list in board like manner
    UPDATED: 12/19/2017
    IN: cell_list a list of numbers or characters
    RETURN: Nothing
    MODIFIES: Nothing
    CALL: Nothing
    Description: It prints a list of numbers or characters in a try/except situation
    if it's a number it's going to add 1 to it and turn it into integer if it couldn't
    turn it into an integer then it's a character and it's going to print it
    """
    count = 0

    for cell in cell_list:
        # if you're in the 3rd column then print a new line
        if count > 2:
            print()
            count = 0

        print ("|",cell,"|" ,end="")

        count = count + 1

# -----------------------------------------------------------------------------------
# player_input
# -----------------------------------------------------------------------------------

def player_input():
    """
    player_input: It asks the user to enter an input
    UPDATED: 12/19/2017
    IN: Nothing
    RETURN: input = an integer that player has chosen
    MODIFIES: Nothing
    CALL: Nothing
    Description: If the input that was provided was greater than 9 or less than 1
    it asks the user for the input again. If the input was -1 it breaks the while loop
    and quits the program. If the input was between 1 and 9 then it returns the input
    """
    while True:
        print()
        input = raw_input("Enter a cell number( enter -1 to quit): ")
        try:
            input = int(input)
        except:
            print ("Enter an integer!")
            continue

        if input == -1:
            answer = raw_input("Do you want to quit? (y/n): ")
            answer = answer.strip()
            if answer[0] == "y":
                sys.exit(0)

        if input < 1 or input > 9:
            print ("Input must be 1 <= input <= 9")
            continue
        else:
            return input

# -----------------------------------------------------------------------------------
# place_marker
# -----------------------------------------------------------------------------------

def place_marker (board_list, marker, position):
    """
    place_marker: places "X" or "O" in the board_list
    UPDATE: 12/21/2017
    IN; board_list = a list of cell to be filled with "X" or "O", marker = "X" or "O" character, position = integer as in where to put the marker
    RETURN: board_list = a list of cells
    MODIFIES: board_list
    CALL: Nothing
    Description: It places "X" or "O" into its position in the list but because list's index starts from
    zero I need to subtract one from it.
    """

    board_list[position - 1] = marker
    return board_list

# -----------------------------------------------------------------------------------
# win_check
# -----------------------------------------------------------------------------------
def win_check (board_list, mark):
    """
    win_check: places "X" or "O" in the board_list
    UPDATE: 12/21/2017
    IN; board_list = a list of cell to be filled with "X" or "O", marker = "X" or "O" character, position = integer as in where to put the marker
    RETURN: board_list = a list of cells
    MODIFIES: board_list
    CALL: Nothing
    Description: It places "X" or "O" into its position in the list but because list's index starts from
    zero I need to subtract one from it.
    """

    # Check the horizental cells
    for step in xrange (0,7,3):
        if board_list[0 + step] == mark and board_list[1 + step] == mark and board_list[2 + step] == mark:
            return True

    # Check the vertical cells
    for step in xrange (0,3):
        if board_list[0 + step] == mark and board_list[3 + step] == mark and board_list[6 + step] == mark:
            return True

    # Check the diameters of board
    for step in xrange (0,3,2):
        if board_list[0 + step] == mark and board_list[4] == mark and board_list[8 - step] == mark:
            return True





# -----------------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------------

def main():
    board_list_list = [0,1,2,"X",4,5,6,7,8,]
    display_board(board_list_list)
    input = player_input()
    board_list_list = place_marker (board_list_list, "X", input)
    display_board (board_list_list)


if __name__ == "__main__":
    main()
