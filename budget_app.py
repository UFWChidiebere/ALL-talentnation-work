class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    # def withdraw(self, amount, description=""):
    #     if self.get_balance >= amount:
    #         amount = -amount
    #         self.ledger.append({'amount': amount, 'description': description})
    #         return True
    #     else:
    #         return False
    # this is the first to be done before the check_balance method is created 
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            amount = -amount
            self.ledger.append({'amount': amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        starting_balance = 0
        for transaction in self.ledger:
            starting_balance += transaction['amount']
        return starting_balance

    # def transfer(self, amount, category):
    #     if self.get_balance() >= amount:
    #         withdrawal_description = f"Transfer to {category.name}"
    #         deposit_description = f"Transfer from {self.name}"
    #         self.withdraw(amount, withdrawal_description)
    #         category.deposit(amount, deposit_description)
    #         return True
    #     return False
    #  the first to be done before the check_balance method is created 

    def transfer(self, amount, category):
        if self.check_funds(amount):
            withdrawal_description = f"Transfer to {category.name}"
            deposit_description = f"Transfer from {self.name}"
            self.withdraw(amount, withdrawal_description)
            category.deposit(amount, deposit_description)

            return True
        return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False 
        else:
            return True


    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        

        items = ""
        for transaction in self.ledger:
            left_align_description = f"{transaction['description'][:23]:<23}"

            right_align_amount = f"{transaction['amount']:>7.2f}"

            items += f"{left_align_description}{right_align_amount}\n"

        total = f"Total: {self.get_balance()}"

        return title + items + total 




def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    
    # 1. Calculate withdrawals per category and total spent overall
    spent_per_cat = []
    total_spent = 0
    for cat in categories:
        cat_spent = sum(-t['amount'] for t in cat.ledger if t['amount'] < 0)
        spent_per_cat.append(cat_spent)
        total_spent += cat_spent

    # Calculate percentages rounded down to the nearest 10
    # Avoid division by zero if nothing has been spent yet
    percentages = []
    for spent in spent_per_cat:
        if total_spent > 0:
            pct = int((spent / total_spent) * 100 // 10) * 10
        else:
            pct = 0
        percentages.append(pct)

    # 2. Build the Y-axis and bars (100 down to 0)
    chart = ""
    for r in range(100, -1, -10):
        chart += f"{r:>3}|"
        for pct in percentages:
            if pct >= r:
                chart += " o "
            else:
                chart += "   "
        chart += " \n" # Strict spacing requires a final space at the end of each row

    # 3. Add the horizontal separator line
    # The line is 3 spaces for numbers + '|' + 3 spaces per category + 1 final space
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Write category names vertically
    max_len = max(len(cat.name) for cat in categories)
    names_section = ""
    for i in range(max_len):
        names_section += "    "
        for cat in categories:
            if i < len(cat.name):
                names_section += f" {cat.name[i]} "
            else:
                names_section += "   "
        names_section += " \n"

    # Remove the very last newline to perfectly match the expected return format
    return title + chart + names_section.rstrip("\n") + " "


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)






class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        entry = f"{'amount': amount, 'description': description}"
        self.ledger.append(entry)

    def withdraw(self, amount, description=""):
        # if self.get_balance() >= amount:
        if self.check_funds(amount):
            amount = -amount
            self.ledger.append(f"{'amount': amount, 'description': description}")
            return True
        else:
            return False

    def get_balance(self):
        starting_balance = 0
        for transaction in self.ledger:
            starting_balance += transaction['amount']
        return starting_balance 

    def transfer(self, amount, category):
        # if self.get_balance() >= amount:
        if self.check_funds(amount):
            withdrawal_description = f"Transfer to {category.name}"
            deposit_description = f"Transfer from {self.name}"
            self.withdraw(amount, withdrawal_description)
            category.deposit(amount, deposit_description)
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        

        items = ""
        for transaction in self.ledger:
            left_align_description = f"{transaction['description'][:23]:<23}"

            right_align_amount = f"{transaction['amount']:>7.2f}"

            items += f"{left_align_description}{right_align_amount}\n"

        total = f"Total: {self.get_balance()}"

        return title + items + total 
    
def create_spend_chart(categories):
    pass