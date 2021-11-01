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
}

profit = 0

isOn = True


def check_resource(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Not enough {ingredient}, sorry :(")
            return False
        return True


def get_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry not enough money.")
        return False


def make_coffe(coffe, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffe} ☕️. Enjoy!🔥\n")


while isOn:
    choice = input(
        "What kind of coffe do you want? (espresso/latte/cappuccino): \nWrite 'report' to see the machine's state or 'off' to exit\n").lower()
    if choice == "off":
        isOn = False
    elif choice == 'report':
        for item in resources:
            print(f'{item}: {resources[item]}')
    else:
        coffe = MENU[choice]
        if check_resource(coffe["ingredients"]):
            payment = get_coins()
            if transaction(payment, coffe["cost"]):
                make_coffe(choice, coffe["ingredients"])
