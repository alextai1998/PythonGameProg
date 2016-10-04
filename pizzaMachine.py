# This section imports the necessary libraries needed for this function
import time
import signal

menu = "1-Margherita, 2-Pepperoni, 3-Hawaiian, C-Cancel, S-Start"
timeout = 0
totalPrice = 0
ptime = 0
MB = 300
MS = 280
PB = 270
PS = 250
HB = 240
HS = 220


while True:
    print(menu)  # Constantly prints the menu

    type = input("Please select the pizza you want. (1~3) ")
    if type == "C":
        continue  # Skips the rest of this loop and starts again
    if int(type) > 3:
        continue  # Skips the rest of this loop and starts again

    size = input("Please select the size you want. (1-Big, 2-Small) ")
    if size == "C":
        continue  # Skips the rest of this loop and starts again
    if int(size) > 2:
        continue  # Skips the rest of this loop and starts again

    cheese = input("Please indicate the number of cheese servings you want. (10NT/serving) ")
    if cheese == "C":
        continue  # Skips the rest of this loop and starts again

    #  This block also assigns the prep time needed and price of order
    if int(type) == 1:
        ptime = 10
        if int(size) == 1:
            p = MB
        else:
            p = MS
    elif int(type) == 2:
        ptime = 5
        if int(size) == 1:
            p = PB
        else:
            p = PS
    else:
        ptime = 8
        if int(size) == 1:
            p = HB
        else:
            p = HS

    totalPrice = p + (int(cheese) * 10)
    print("Total price is: %r" % totalPrice)
    print("Start? (S-Start) ")

    signal.alarm(timeout)
    decision = input()
    signal.alarm(0)
    if decision == "S":
        print("Seconds remaining: ")
        print(ptime)
        while ptime > 0:
            time.sleep(1)
            ptime -= 1
            print(ptime)
        print("READY")
        break
    else:
        continue
