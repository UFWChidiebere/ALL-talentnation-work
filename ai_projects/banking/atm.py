balance = 1000
print("🏦 Welcome to your Terminal ATM App! 🏦")
print(f"Starting balance state: ₦{balance}\n")
while balance > 0:
    amount_str = input("How much do you want to withdraw? (Type 0 to leave): ")
    withdrawal = int(amount_str)
    if withdrawal == 0:
        print("Transaction ended.")
        break
    if withdrawal > balance:
        print("❌ Transaction Declined! Insufficient funds.")
    else:
        balance = balance - withdrawal
        print(f"✅ Success! Your balance state transformed to: ₦{balance}")
print(f"\nFinal account state saved. Total left: ₦{balance}")
