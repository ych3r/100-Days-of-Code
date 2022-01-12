MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO: 1. Print report.
def print_report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


# TODO: 2. Check resources sufficient?
def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        return True


# TODO: 3. Process coins.
def process_coins(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)


# TODO: 4. Check transaction successful?
def check_transaction(drink, paid):
    if paid < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if paid > MENU[drink]["cost"]:
            print(f"Here is ${paid - MENU[drink]['cost']} in change.")
        resources["money"] += MENU[drink]["cost"]
        return True


# TODO: 5. Make Coffee.
def make_coffee(drink):
    if check_resources(drink):
        paid = process_coins(drink)
        if check_transaction(drink, paid):
            print(f"Here is your {drink}. Enjoy!")


def main():
    end = False
    while not end:
        req = input("What would you like? (espresso/latte/cappuccino): ")
        if req == "report":
            print_report()
        elif req == "off":
            end = True
        elif req == "espresso":
            make_coffee(req)
        elif req == "latte":
            make_coffee(req)
        elif req == "cappuccino":
            make_coffee(req)


main()
