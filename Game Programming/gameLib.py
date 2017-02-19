# """
# This program serves as a library for all of the functions Alex wrote for Game Programming.
# """
#
# import sys, tty, termios
#
#
# def getkey():
#     fd = sys.stdin.fileno()
#     old_setting = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)
#     return ch


dict = {'x': 5, 'y': 5}

if {'x': 5, 'y': 5} in list:
    print("{'x': 5, 'y': 5} is in list!")


print(list[0])
