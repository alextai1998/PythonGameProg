# This section imports the necessary libraries needed for this function
import time

now = time.clock()
future = now + 10
print(now)

menu = "1-Latte, 2-Americano, 3-Espresso, C-Cancel, S-Start"
tempPrice = 0


while True:
    print(menu)  # Constantly prints the menu

    # This section asks for the input
    value = input("Please select the coffee you want. (1~3) ")
    if value == "C":
        continue  # Skips the rest of this loop and starts again
    else:
        coffeeType = value

    # This section asks for the input
    value = input("Please select the size you want. (1-Big, 2-Small) ")
    if value == "C":
        continue  # Skips the rest of this loop and starts again
    else:
        size = value

    # This section asks for the input
    value = input("Please indicate the number of sugar servings you want. (0~5) ")
    if value == "C":
        continue  # Skips the rest of this loop and starts again
    else:
        sugar = value

    #  This following block assigns the temporary prices w/o the price of sugar

    #  This block also assigns the prep time needed
    if int(coffeeType) == 1 and int(size) == 1:
        tempPrice = 30
        prepTime = 6
    elif int(coffeeType) == 1 and int(size) == 2:
        tempPrice = 20
        prepTime = 6
    elif int(coffeeType) == 2 and int(size) == 1:
        tempPrice = 50
        prepTime = 4
    elif int(coffeeType) == 2 and int(size) == 2:
        tempPrice = 30
        prepTime = 4
    elif int(coffeeType) == 3 and int(size) == 1:
        tempPrice = 40
        prepTime = 5
    elif int(coffeeType) == 3 and int(size) == 2:
        tempPrice = 25
        prepTime = 5

    #  This part is pretty self explanatory, it prints the total price
    price = int(sugar) + tempPrice
    print(price)

    #  Asks if user wishes to start
    value = input("Start? (S-Start) ")

    if value == "S":
        print("Please wait for %r seconds!" % prepTime)
        time.sleep(prepTime)
        print("READY")
