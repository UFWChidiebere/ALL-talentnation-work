def change_string(string):
    if string == "":
        return ""
    return change_string(string[1:]) + string[0]
print(change_string("wisdom"))