def safe_calculator(a, operator, b):
    pass
    operator_1 = ["+", "-", "*", "/", "%", "**"]
    if (operator_1 == "/" or operator_1 == "%") and b == 0:
        return "Cannot divide by zero"
    if operator_1 not in operator_1:
        return "Invalid operator"
    elif operator_1 == "+":
        return a + b
    elif operator_1 == "-":
        return a - b
    elif operator_1 == "*":
        return a * b
    elif operator_1 == "/":
        return round(a / b, 2)
    elif operator_1 == "%":
        return a % b
