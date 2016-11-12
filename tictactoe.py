"""
This program allows a player to play tic tac toe w/ an AI.
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


def winner(plays):
    """
    Checks the winner of the game
    :param plays: A dictionary that includes the locations and the values of the grid
    :return: True there is a winner
    """
    return (plays[1] == plays[2] == plays[3] and plays[1] != " ") or\
           (plays[4] == plays[5] == plays[6] and plays[4] != " ") or\
           (plays[7] == plays[8] == plays[9] and plays[7] != " ") or\
           (plays[1] == plays[4] == plays[7] and plays[1] != " ") or\
           (plays[2] == plays[5] == plays[8] and plays[2] != " ") or\
           (plays[3] == plays[6] == plays[9] and plays[3] != " ") or\
           (plays[1] == plays[5] == plays[9] and plays[1] != " ") or\
           (plays[3] == plays[5] == plays[7] and plays[3] != " ")


def update_board(plays):
    loc_filled = 0
    chosen_coor = []

    while loc_filled < 9:
        if loc_filled % 2 == 0:
            print("| O's Turn |")
            symbol = "O"
        else:
            print("| X's Turn |")
            symbol = "X"

        location = input("Please input a coordinate (1~9): ")

        if location in chosen_coor:
            print("That spot is already taken!")
            continue

        plays[location] = symbol
        chosen_coor.append(location)

        loc_filled += 1
        display_grid(plays)
        win = winner_check(plays)

        if win:
            if symbol == "X":
                print("")
                print("***********************")
                print("***********************")
                print("***                 ***")
                print("***     X  WINS     ***")
                print("***                 ***")
                print("***********************")
                print("***********************")
                exit()
            else:
                print("")
                print("***********************")
                print("***********************")
                print("***                 ***")
                print("***     O  WINS     ***")
                print("***                 ***")
                print("***********************")
                print("***********************")
                exit()
    print("")
    print("***********************")
    print("***********************")
    print("***                 ***")
    print("***   IT IS A TIE   ***")
    print("***                 ***")
    print("***********************")
    print("***********************")


def winner_check(data):
    """
    Combines 3 functions above into one.
    :param plays: A dictionary that includes the locations and the values of the grid
    :return: True if a winner is determined, false if not
    """

    if turn["human"] == "X":
        if x_winner_check(data["grid"]):
            data["score"] += 10
        elif o_winner_check(data("grid")):
            data["score"] -= 10
    else:
        if x_winner_check(data["grid"]):
            data["score"] -= 10
        elif o_winner_check(data("grid")):
            data["score"] += 10


def generate_children(data):
    """
    generates all possible moves in the game
    :param data: dictionary grid, turn, score, children
    :return children: a list of data
    """
    children = []
    score = 0
    for key, value in gridStruct["grid"].items():
        if value == " ":
            gridChild = boardValues.copy()
            gridChild[key] = data["turn"]
            nextTurn = "X" if data["turn"] == "O" else "O"
            display_grid(gridChild)
            print(" ")
            if winner_check(gridChild):
                score += 10
                gridStructChild = {'grid': gridChild,
                                   'score': score,
                                   'turn': nextTurn,
                                   'children': None}
                children.append(gridStructChild)
    return children


boardValues = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}  # Initializes the board
turn = {"human": "X", "machine": "O"}

firstPlayer = input("Who should go first? Human or Machine? (H/M) ")
if firstPlayer.upper() == "M":
    turn = {"human": "O", "machine": "X"}
    gridStruct = {"grid": boardValues,
                  "score": None,
                  "children": None,
                  "turn": turn["machine"]}
else:
    gridStruct = {"grid": boardValues,
                  "score": None,
                  "children": None,
                  "turn": turn["human"]}

availableCoor = []
cells = boardValues.values()
for i in cells:
    if i == " ":
        availableCoor.append(i)
numPossible = len(availableCoor)


def generateChildren(data):
    '''
    generates all possible moves in the game
    :param data: dictionary grid, turn, score, children
    :return children: a list of data
    '''
    children = []
    score = 0
    for key, value in data['grid'].items():
        if value == ' ':
            gridChild = grid.copy()
            gridChild[key] = data['turn']
            nextTurn = 'x' if data['turn']=='o' else 'o'
            print(' ')
            if(tttLib.winner(gridChild)):
                tttLib.displayGrid(gridChild)
                if(gridChild[key] == 'x'):
                    if(turn['human'] == 'x'):
                        score += 10
                    else:
                        score -= 10
                else:
                    if(turn['human'] == 'o'):
                        score += 10
                    else:
                        score -= 10
                gridStructChild = {'grid': gridChild,
                                   'score':score,
                                   'turn':nextTurn,
                                   'children':None}
                children.append(gridStructChild)
    print score
    return children

children = generateChildren(data)
