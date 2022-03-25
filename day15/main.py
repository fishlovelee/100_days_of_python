from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


# TODO: 1. Print Report of all Resources.
def report_resource():
    formatted_string = f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}"
    print(formatted_string)


# TODO: 2. Check Resources Sufficient
def check_resource_sufficient(drink_type):
    """Given the drink type, return if the drink resource is sufficient."""
    drink_resource = MENU[drink_type]
    for key in drink_resource["ingredients"]:
        if drink_resource["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


# TODO: 3. Process Coins.
def process_coins():
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


# TODO: 4. Check transaction successful?
def process_transaction(inserted_total, drink_cost):
    change_amount = inserted_total - drink_cost
    if change_amount > 0:
        print(f"Here's your ${round(change_amount, 2)} dollars in change")
    elif change_amount < 0:
        print("Sorry that's not enough money. Money refunded")
    return change_amount >= 0


# TODO: 5. Make coffee.
def make_coffee(drink_type):
    coffee = MENU[drink_type]
    for ingredient in coffee["ingredients"]:
        resources[ingredient] -= coffee["ingredients"][ingredient]
    resources["money"] += coffee["cost"]
    print(f"Here's your {drink_type} ☕")


def coffee_machine():
    print(logo)
    machine_on = True
    while machine_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino):")
        if user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            report_resource()
        else:
            resource_sufficient = check_resource_sufficient(user_choice)
            if resource_sufficient:
                if process_transaction(process_coins(), MENU[user_choice]["cost"]):
                    make_coffee(user_choice)


coffee_machine()