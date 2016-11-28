def calc(x):
    """
    This is a recursive function to find the factorial of an integer
    :param x: Random integer
    :return: Factorial of an integer
    """

    if x == 1:
        return 1
    else:
        return x * calc(x-1)

num = 4
print("The factorial of ", num, " is ", calc(num))
