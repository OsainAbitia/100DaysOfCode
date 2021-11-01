from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

isOn = True

while isOn:
    options = menu.get_items()
    choice = input(f"What kind of coffee do you want? ({options}):\n")
    if choice == "off":
        isOn = False
    elif choice == 'report':
        print(coffeeMaker.report())
        print(moneyMachine.report())
    else:
        coffee = menu.find_drink(choice)
        enoughIngredients = coffeeMaker.is_resource_sufficient(coffee)
        enoughPayment = moneyMachine.make_payment(coffee.cost)
        if enoughIngredients and enoughPayment:
            coffeeMaker.make_coffee(coffee)
