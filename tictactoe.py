"""
This program allows two players to play tic tac toe.
"""


def displayGrid(plays):
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

def update():



boardValues = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}


displayGrid(boardValues)
