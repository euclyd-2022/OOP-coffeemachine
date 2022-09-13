from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
money= MoneyMachine()
menu = Menu()
drinklist=menu.get_items()

machineison=True
while machineison:
    choice=input(f"Please select a drink? {drinklist}: ")

    if choice == "report":
       print(coffeemaker.report())
       print(money.report())

    elif choice=="off":
        machineison=False
    else:
        drink = menu.find_drink(choice)

        if coffeemaker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
           coffeemaker.make_coffee(drink)






