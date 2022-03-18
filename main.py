import sys


def coffeeInput():
    """Awaits input for coffee choice"""
    print("What would you like? (Espresso/Latte/Cappuccino):")
    selection = input()
    return selection

coffees = {
    "Espresso" : [100, 100, 350, 1.25],
    "Latte" : [200, 350, 150, 1.75],
    "Cappuccino" : [300, 280, 200, 2.75]
}

resources = [
    {"Water" : 1000},
    {"Milk" : 1000},
    {"Coffee" : 1000},
    {"Money" : 0}
]

bankAcct = 0
onFlag = True
water = int(resources[0]["Water"])
milk = int(resources[1]["Milk"])
coffee = int(resources[2]["Coffee"])

def quit():
    global onFlag
    onFlag = False
    print("Powering off...")
    sys.exit("")

def start():
    """"Starts the machine"""
    while onFlag:
        verifyTransaction()


def report():
    """"Prints report of available resources"""
    print(f"Water: {resources[0]['Water']} \nMilk: {resources[1]['Milk']} \nCoffee: {resources[2]['Coffee']} \nMoney: {resources[3]['Money']} ")



def verifyTransaction():
    """Allows user to insert coins and verifies transaction"""
    global bankAcct
    global water
    global milk
    global coffee

    inputCof = coffeeInput().title()
    if inputCof == "Report":
        report()
        start()
    elif inputCof == "Quit":
        quit()

    quarters = float(input("How many quarters: ")) * .25
    dimes = float(input("How many dimes: ")) * .10
    nickels = float(input("How many nickels: ")) * .05
    pennies = float(input("How many pennies: ")) * .01
    total = quarters + dimes + nickels + pennies
    if total >= 1.25 and inputCof == "Espresso" or total >= 1.75 and inputCof == "Latte" or total >= 2.75 and inputCof == "Cappuccino":
        if resources[0]["Water"] < coffees[inputCof][0] or resources[1]["Milk"] < coffees[inputCof][1] or resources[2]["Coffee"] < coffees[inputCof][2]:
            print("Sorry, there is not enough water")
            start()
        water -= coffees[inputCof][0]
        milk -= coffees[inputCof][1]
        coffee -= coffees[inputCof][2]
        bankAcct += coffees[inputCof][3]
        resources[3].update({"Money": bankAcct})
        resources[1].update({"Milk": milk})
        resources[0].update({"Water": water})
        resources[2].update({"Coffee": coffee})
        change = total - coffees[inputCof][3]
        print(f"Here's your {inputCof}. Your change is {change:.2f}. Enjoy!")
    else:
        print("Sorry that's not enough. Refunding money")




start()

