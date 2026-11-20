'''STEP 1: Define 'get_income(transactions)'
        - Use filter() to keep only items where transaction["type"] == "income".
        - Return the filtered list.

STEP 2: Define 'get_expenses(transactions)'
        - Use filter() to keep only items where transaction["type"] == "expense".
        - Return the filtered list.

STEP 3: Define 'calculate_total(amounts)'
        - Create a variable 'total' = 0.
        - Loop through each amount and add it to 'total'.
        - Return 'total'.

STEP 4: Define 'find_largest(expense_list)'
        - If the list is empty, return None.
        - Create a variable 'largest_item' = first expense item in the list.
        - Loop through the rest of the expenses:
            - If current item's amount > largest_item's amount, update largest_item.
        - Return 'largest_item'.

STEP 5: Define 'get_balance(income, expenses)'
        - Return (income minus expenses).

STEP 6: Define 'get_status(balance)'
        - If balance > 0, return "Positive balance"
        - If balance < 0, return "Negative balance"
        - If balance == 0, return "Break-even"

STEP 7: Build the final 'analyze(transactions)' pipeline (The Hard Bonus)
        - Call filtering functions to get raw lists of incomes and expenses.
        - Use map() to extract just the numbers/amounts out of the lists.
        - Call calculate_total() on those amounts to find total income and total expenses.
        - Compute balance, status, and find the largest expense.
        - Package everything nicely into a single dictionary and return it.
'''

# --- STEP 1 & 2: Sifting Transactions with Filter ---

def get_income(transactions: list[dict]) -> list[dict]:
    """Pure function filtering only income types."""
    return list(filter(lambda t: t["type"] == "income", transactions))

def get_expenses(transactions: list[dict]) -> list[dict]:
    """Pure function filtering only expense types."""
    return list(filter(lambda t: t["type"] == "expense", transactions))


# --- STEP 3: Manual Aggregate Math Calculator ---

def calculate_total(amounts: list[float]) -> float:
    """Manually aggregates a list of numbers without using sum()."""
    total = 0.0
    for amt in amounts:
        total += amt
    return total


# --- STEP 4: Manual Extremes Search Tracker ---

def find_largest(expense_list: list[dict]) -> dict | None:
    """Manually tracks the largest single expense dictionary without max()."""
    if not expense_list:
        return None
        
    largest_item = expense_list[0]
    for item in expense_list:
        if item["amount"] > largest_item["amount"]:
            largest_item = item
            
    return largest_item


# --- STEP 5 & 6: Balances and Status Classifiers ---

def get_balance(income_total: float, expense_total: float) -> float:
    """Pure mathematical net ledger balance tracker."""
    return income_total - expense_total

def get_status(balance: float) -> str:
    """Determines financial status based on total balance."""
    if balance > 0:
        return "Positive balance"
    elif balance < 0:
        return "Negative balance"
    else:
        return "Break-even"


# --- 🟢 GREEN BONUS: General Filter Function ---

def filter_transactions(transactions: list[dict], condition_fn) -> list[dict]:
    """Higher-order filter function applying a dynamic condition argument rule."""
    return list(filter(condition_fn, transactions))


# --- 🔴 RED HARD BONUS: Unified Master Pipeline Analyzer ---

def analyze(transactions: list[dict]) -> dict:
    """Assembles all underlying sub-functions to yield a final record map metrics profile."""
    # 1. Isolate and capture item records lists
    # (Using the green bonus function with a lambda here for income as requested!)
    income_records = filter_transactions(transactions, lambda t: t["type"] == "income")
    expense_records = get_expenses(transactions)
    
    # 2. Map arrays down into simple pure float/int lists
    income_amounts = list(map(lambda t: t["amount"], income_records))
    expense_amounts = list(map(lambda t: t["amount"], expense_records))
    
    # 3. Aggregate arithmetic calculations manually
    total_inc = calculate_total(income_amounts)
    total_exp = calculate_total(expense_amounts)
    
    # 4. Process secondary metrics indicators
    net_balance = get_balance(total_inc, total_exp)
    financial_status = get_status(net_balance)
    
    # 5. Extract item markers
    top_expense_node = find_largest(expense_records)
    largest_expense_name = top_expense_node["name"] if top_expense_node else "None"
    
    # Track the count of expenses manually using list length or a manual count
    expense_count = 0
    for _ in expense_records:
        expense_count += 1

    # 6. Bundle results into the required dictionary layout map
    return {
        "income": total_inc,
        "expenses": total_exp,
        "balance": net_balance,
        "largest_expense": largest_expense_name,
        "expense_count": expense_count,
        "status": financial_status
    }


# --- STEP 7: Main Executive Runner Block (Printing strictly outside) ---
if __name__ == "__main__":
    # --- Dataset 1: Standard Challenge Data ---
    starting_transactions = [
        {"name": "Laptop", "amount": 250000, "type": "expense"},
        {"name": "Salary", "amount": 500000, "type": "income"},
        {"name": "Internet", "amount": 30000, "type": "expense"},
        {"name": "Freelance", "amount": 150000, "type": "income"},
        {"name": "Food", "amount": 45000, "type": "expense"}
    ]
    
    print("=== STANDALONE EXPECTED PRINT PATTERN ===")
    # Manual evaluation matching your base prompt expectations
    inc_list = get_income(starting_transactions)
    exp_list = get_expenses(starting_transactions)
    
    inc_total = calculate_total(list(map(lambda t: t["amount"], inc_list)))
    exp_total = calculate_total(list(map(lambda t: t["amount"], exp_list)))
    bal = get_balance(inc_total, exp_total)
    big_exp = find_largest(exp_list)
    
    print(f"Total income: {int(inc_total)}")
    print(f"Total expenses: {int(exp_total)}")
    print(f"Balance: {int(bal)}")
    if big_exp:
        print(f"Largest expense: {big_exp['name']} ({big_exp['amount']})")
    print(f"Number of expenses: {len(exp_list)}")
    print(f"Status: {get_status(bal)}")

    print("\n=== 🔴 RED HARD BONUS DICTIONARY RETURN TEST ===")
    
    # Test 1: Standard transactions
    print("Standard Data:")
    print(analyze(starting_transactions))
    
    # Test 2: Edge case - Completely empty array input
    print("\nEdge Case: Empty List []")
    print(analyze([]))
    
    # Test 3: Edge case - Only income transaction present
    print("\nEdge Case: Only Salary")
    print(analyze([{"name": "Salary", "amount": 500000, "type": "income"}]))
