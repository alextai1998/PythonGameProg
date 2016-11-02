"""
This program allows two players to play tic tac toe.
"""


def display_grid(plays):
    """
    Prints out grid and values
    :param plays: A dictionary that includes the locations and the values of the grid
    :return: none
    """

    print("The board looks like this now:")
    print("")
    print("         |         |         ")
    print("    %s    |    %s    |    %s    " % (plays[1], plays[2], plays[3]))
    print("         |         |         ")
    print("-----------------------------")
    print("         |         |         ")
    print("    %s    |    %s    |    %s    " % (plays[4], plays[5], plays[6]))
    print("         |         |         ")
    print("-----------------------------")
    print("         |         |         ")
    print("    %s    |    %s    |    %s    " % (plays[7], plays[8], plays[9]))
    print("         |         |         ")


def update_x():
    """
    Prompts Player 1 to enter a play and then updates the board
    :return: None
    """
    while True:
        location = int(input("Please input where you want to place X: "))
        if location not in boardValues:
            print("That spot is not on the board!")
            continue
        else:
            if empty_check(location):
                boardValues[location] = "X"
                break
            else:
                print("That spot is already taken!")


def update_o():
    """
    Prompts Player 2 to enter a play and then updates the board
    :return: None
    """
    while True:
        location = int(input("Please input where you want to place O: "))
        if location not in boardValues:
            print("That spot is not on the board!")
            continue
        else:
            if empty_check(location):
                boardValues[location] = "O"
                break
            else:
                print("That spot is already taken!")


def empty_check(loc):
    """
    Checks if the spot entered is empty
    :param loc: An integer that indicates the location
    :return: Returns true if the location is empty
    """
    return boardValues[loc] == " "


def x_winner_check(plays):
    """
    Checks if Player 1 wins the game
    :param plays: A dictionary that includes the locations and the values of the grid
    :return: True if Player 1 wins
    """
    return (plays[1] == "X" and plays[2] == "X" and plays[3] == "X") or\
    (plays[4] == "X" and plays[5] == "X" and plays[6] == "X") or\
    (plays[7] == "X" and plays[8] == "X" and plays[9] == "X") or\
    (plays[1] == "X" and plays[4] == "X" and plays[7] == "X") or\
    (plays[2] == "X" and plays[5] == "X" and plays[8] == "X") or\
    (plays[3] == "X" and plays[6] == "X" and plays[9] == "X") or\
    (plays[1] == "X" and plays[5] == "X" and plays[9] == "X") or\
    (plays[3] == "X" and plays[5] == "X" and plays[7] == "X")


def o_winner_check(plays):
    """
    Checks if Player 2 wins the game
    :param plays: A dictionary that includes the locations and the values of the grid
    :return: True if Player 2 wins
    """
    return (plays[1] == "O" and plays[2] == "O" and plays[3] == "O") or\
    (plays[4] == "O" and plays[5] == "O" and plays[6] == "O") or\
    (plays[7] == "O" and plays[8] == "O" and plays[9] == "O") or\
    (plays[1] == "O" and plays[4] == "O" and plays[7] == "O") or\
    (plays[2] == "O" and plays[5] == "O" and plays[8] == "O") or\
    (plays[3] == "O" and plays[6] == "O" and plays[9] == "O") or\
    (plays[1] == "O" and plays[5] == "O" and plays[9] == "O") or\
    (plays[3] == "O" and plays[5] == "O" and plays[7] == "O")


def tie_check(plays):
    """
    Checks if the board is full/tied
    :param plays: A dictionary that includes the locations and the values of the grid
    :return: True is board is full/tied
    """
    x = list(plays.values())  # Gets a list of the values in the dictionary plays
    return " " not in x  # This means that it is full


def display_winner(player):
    """
    Displays the winner
    :param player: An integer indicating winner
    :return: None
    """
    print("")
    print("***********************")
    print("***********************")
    print("***                 ***")
    print("***  PLAYER %d WINS  ***" % player)
    print("***                 ***")
    print("***********************")
    print("***********************")


def display_tie():
    """
    Displays the result Tie
    :return: None
    """
    print("")
    print("***********************")
    print("***********************")
    print("***                 ***")
    print("***   IT IS A TIE   ***")
    print("***                 ***")
    print("***********************")
    print("***********************")


boardValues = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}  # Initializes the board
display_grid(boardValues)  # Displays starting board


while True:
    # Player 1's Turn
    update_x()
    display_grid(boardValues)
    if x_winner_check(boardValues):
        display_winner(1)
        break

    # Tie Check after Player 1's Turn
    if tie_check(boardValues):
        display_tie()
        break

    # Player 2's Turn
    update_o()
    display_grid(boardValues)
    if o_winner_check(boardValues):
        display_winner(2)
        break

    # Tie Check after Player 1's Turn
    if tie_check(boardValues):
        display_tie()
        break
