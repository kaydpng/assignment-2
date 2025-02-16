
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """
        Function to check if the required ingredients are available.
        Returns False if ingredients are insufficient or unavailable, otherwise True
        """
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] < amount:
                print(f"We dont have enough {ingredient}!")
                return False
            if ingredient not in self.machine_resources:
                print(f"We dont have {ingredient}!")
                return False
        return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        """ Deducts required ingredients to make the sandwich. """
        for ingredient, amount in order_ingredients.items():
            if ingredient in self.machine_resources:
                self.machine_resources[ingredient] -= amount
        print(f"Here is your {sandwich_size} sandwich!")

    def report(self):
        """ Prints report of amount of remaining ingredients. """
        print("Report: ")
        for ingredient, amount in self.machine_resources.items():
            print(f"{ingredient}: {amount}")