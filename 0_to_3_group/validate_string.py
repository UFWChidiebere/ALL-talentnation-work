def validate_length(string):
    n = len(string)
    if n < 8:
           print(f"Length {n} is too short, needs at least 8")
    else:
        print(f"Length {n} is okay!")

validate_length("Pythonista")

validate_length("Python")


'''to use the walrus operator we do not need to declare a variable n..... we still need it but the walrus operator will allow us to declare it and assign and use it inside the if statement 

as senn in the code below'''

def validate_length_of_string(string):
     if (n := len(string)) < 8:
          return f"The length of {n} is too short, need at least 8 char."
     else:
          return f"The length of {n} is okay! you can proceed to use it for whatever you want to use it for."
k1 = "thisisthenameoftheprogram"
k2 = "come"

print(validate_length_of_string(k1))
print(validate_length_of_string(k2))



'''note: using the walrus operator must be followed by a parentheses so that python can calculate result efficiently..... why coz  the walrus operator has a lower operator-precedence'''