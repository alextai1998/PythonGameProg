def coeffs(r, c):
    """
    Calculates the coefficients using input to stop recursion
    :param r: Number of rows
    :param c: Number of columns left in that row
    :return:
    """
    if c == 0 or c == r:
        return 1
    return coeffs(r-1, c-1) + coeffs(r-1, c)


def generateCoeffs(rows):
    """
    Generates the Pascal Triangle
    :param rows: int
    :return: None
    """
    for row in range(rows):
        answer = ""
        for column in range(row + 1):
            answer = answer + str(coeffs(row, column)) + " "
        print(answer.center(50))

generateCoeffs(5)
