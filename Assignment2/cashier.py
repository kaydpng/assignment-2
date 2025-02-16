class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """
        Function to process user input for coins.
        Prompts user to insert amounts of coins and calculates the total.
        Return total amount.
        """
        print("Please insert coins.")
        dollars = float(input("How many large dollars?: "))
        halves = float(input("How many half dollars?: "))
        quarters = float(input("How many nickles?: "))
        nickels = float(input("How many pennies?: "))
        return float(dollars * 1.00) + (halves * 0.5) + (quarters * 0.25) + (nickels * 0.05)


    def transaction_result(self, coins, cost):
        """
        Function to handle transaction.
        Compares coins and cost and returns True is enough money was inserted.
        If amount is insufficient, refund the money and return False
        """
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print(f"Sorry that's not enough money. Money refunded.")
            return False