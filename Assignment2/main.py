import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():


    while True:
        input1 = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        if input1 == "off":
            print("Goodbye!")
            break
        elif input1 == "report":
            sandwich_maker_instance.report()
        elif input1 in recipes:
            order = input1
            if sandwich_maker_instance.check_resources(recipes[order]["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, recipes[order]["cost"]):
                    sandwich_maker_instance.make_sandwich(order, recipes[order]["ingredients"])
            else:
                print("Check back later, ingredients are low!")
        else:
            print("ERROR!!")

if __name__=="__main__":
    main()
