import pyttsx3

class BankAccount:
    def __init__(self, owner_name, balance = 0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: amount to be deposited must be greater than 0")
        else:
            self.balance += amount    
            print(f"Deposited  ${amount}. New Balance: ${self.balance}")

    def withdrawal(self, amount):
        if amount <= 0:
            print("Error: withdrawal must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful! Remaining Balance: ${self.balance}")

    def speak_balance(self):
        engine = pyttsx3.init()
        engine.setProperty( 'rate', 150)

        message =  f"Hello {self.owner_name}, your current balance is {self.balance} dollars"

        print(f"\nSpeaking: '{message}'")
        engine.say(message)
        engine.runAndWait()

class SavingsAccount(BankAccount):
    def __init__(self, owner_name, balance=0, interest_rate=0.02):
        super().__init__(owner_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(f"Interest applied! Earned: ${'interest_earned.2f'}. New Balance: ${'self.balance.2f'}")


# --- TESTING ZONE ---
# 1. Open an account for yourself with an initial deposit
my_account = BankAccount("Gamp", 500)

# 2. Test the actions
my_account.deposit(200)       # Should show $700
my_account.withdrawal(100)    # Should show $600
my_account.withdrawal(1000)   # Should trigger "Insufficient funds!"

# 3. Hear it live!
my_account.speak_balance()




# --- TESTING THE CHILD CLASS ---
# 1. Create a savings account instance (with a 5% interest rate)
my_savings = SavingsAccount("Gamp", 1000, 0.05)

# 2. Look! We can use deposit even though it's not written in SavingsAccount!
my_savings.deposit(500)      # Balance becomes $1500

# 3. Use the unique child method
my_savings.apply_interest()  # Calculates 5% of $1500 ($75) and adds it!

# 4. Use the parent speech method!
my_savings.speak_balance()   # Speaks your new total ($1575) aloud!

