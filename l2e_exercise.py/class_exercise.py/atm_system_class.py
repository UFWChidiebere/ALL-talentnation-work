class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
        self.counter = []

    def check_balance(self):
        print(f"Your balance is {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount: Deposit cannot be negative or 0.")
            
            return
        self.balance += amount
        self.counter.append(("Credited",amount))
        print(f"deposit successful: New balance is ${self.balance}")
        # self.counter +=1

    def withdrawal(self, amount, pin):
        if not self.pin and len(pin) != 4:
            print("Incorrect Pin")
            return
        # elif pin != self.pin:
        #     print("Incorrect Pin")
        elif amount <= 0:
            print("Invalid Amount: withdrawal must be greater than zero")
            return
        elif amount > self.balance:
            print("Insuuficient Funds!")
            return
        else:
            self.balance -= amount
            self.counter.append(("Debited",amount))
            print(f"Withdrawal successful: ${amount}. New balance ${self.balance}")

    def change_pin(self, old_pin, new_pin):
        if self.pin!=old_pin:
            return
        elif len(new_pin)!=4:
            print("Pin must be 4-digits")
        elif not new_pin.isdigit():
            print('invalid pin')
            return
        else:
            self.pin=new_pin

    def show_history(self):
        k=1
        for status,amount in self.counter:
            print(k,".",status,amount)
            k+=1



cus1 = ATM(500000, "1234")

cus1.withdrawal(100000, "1234")
cus1.withdrawal(100000, "12345")
cus1.deposit(200000)
cus1.show_history()










"""This code is same as the above just that it is of a different logic and it uses 'try and except' and it was written by Maria Okunribido"""


class ATM:
    def __init__(self, balance: int, pin: int):
        self.balance = balance
        self.pin = pin
        self.counter = 0

    def check_balance(self):
        print(f"Your balance is {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        else:
            self.balance += amount
            self.counter += 1

    def withdraw(self, amount, pin):
        if self.balance < amount:
            raise ValueError("Insufficient Funds!")
        attempts = 3
        while attempts > 0:
            user_input = input("Please enter your transaction pin: ")
            if user_input.isdigit() and int(user_input) == self.pin:
                self.balance -= amount
                self.counter += 1
                print("Withdrawal Successful!")
                return
            else:
                attempts -= 1
                if attempts == 2:
                    print("Incorrect Pin: you have two(2) more trials.")
                elif attempts == 1:
                    print("Incorrect Pin: you have one(1) more trials.")
                elif attempts == 0:
                    raise ValueError("Incorrect Pin: Goodbye")

    def change_pin(self, old_pin, new_pin):
        old_pin = input("Type your old pin: ")
        """validate and check the old pin"""
        if not old_pin.isdigit() or int(old_pin) != self.pin:
            print("Your pin is incorrect.")
            return
        new_pin = input("Type your new pin: ")
        '''check if the new pin is numeric and up to 4 and nor more than 4'''
        if not new_pin.isdigit() or int(new_pin) != 4:
            print("Pin must be number and must contain at least and at most four(4) character.")
            return
        else:
            self.pin = int(new_pin)
            print("Pin changed successfully.")

    def show_history(self):
            k=1
            for status,amount in self.counter:
                print(k,".",status,amount)
                k+=1



"""when i pasted the above code maria gave me on AI, some things were wrong and it was corrected. though the show_history method was inputed by me 
below is the AI optimized and corrected code """

class ATM:
    def __init__(self, balance: int, pin: int):
        self.balance = balance
        self.pin = pin
        # FIXED: Changed integer counter to an empty list for tracking history
        self.history = [] 

    def check_balance(self):
        print(f"Your balance is ₦{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        
        self.balance += amount
        # FIXED: Tracking history items dynamically
        self.history.append(("Deposit", amount))
        print(f"Successfully deposited ₦{amount}.")

    # FIXED: Removed unused 'pin' argument from method definition
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient Funds!")
            
        attempts = 3
        while attempts > 0:
            user_input = input("Please enter your transaction pin: ")
            if user_input.isdigit() and int(user_input) == self.pin:
                self.balance -= amount
                # FIXED: Logging to history list
                self.history.append(("Withdrawal", amount))
                print("Withdrawal Successful!")
                return
            else:
                attempts -= 1
                if attempts == 2:
                    print("Incorrect Pin: you have two(2) more trials.")
                elif attempts == 1:
                    print("Incorrect Pin: you have one(1) more trials.")
                elif attempts == 0:
                    raise ValueError("Incorrect Pin: Account locked. Goodbye.")

    # FIXED: Cleaned up parameters since inputs are gathered inside the method
    def change_pin(self):
        old_pin = input("Type your old pin: ")
        if not old_pin.isdigit() or int(old_pin) != self.pin:
            print("Your pin is incorrect.")
            return
            
        new_pin = input("Type your new pin: ")
        # FIXED: Validating length of string instead of its integer value
        if not new_pin.isdigit() or len(new_pin) != 4:
            print("Pin must be numeric and exactly four (4) characters long.")
            return
            
        self.pin = int(new_pin)
        print("Pin changed successfully.")

    def show_history(self):
        # FIXED: Safely looping through history tuples using enumerate()
        if not self.history:
            print("No transactions recorded yet.")
            return
            
        print("\n--- Transaction History ---")
        for k, (status, amount) in enumerate(self.history, start=1):
            print(f"{k}. {status}: ₦{amount}")

    