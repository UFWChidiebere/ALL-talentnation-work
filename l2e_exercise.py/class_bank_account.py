class BankAcount:
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Error: amount should be grater than 0.")
        elif amount > 0:
            self.balance += amount
            print(f"Transaction successful: deposited amount #{amount}. New Balance #(self.balance)")
        else:
            print("Inavlid Transaction")

    def withdrawal(self,amount):
        if amount <= 0:
            print("amount to be dopisited must be greater than 0")
        elif amount > self.balance:
            print("Insufficient funds!")
        elif amount < self.balance:
            self.balance -=amount
            print(f"withdrawal successful:  New Balance is #{self.balance}")
        else:
            print("Invalid Trasaction")

    def check_balance(self):
        print(f"Thank you {self.account_name} for requesting for your balance. Your account available balance is {self.balance}.")

bank = BankAcount("Wisdom", "123456789", 10000)
print(bank.balance)
