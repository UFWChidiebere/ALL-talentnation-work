# def censored_word(text, banned_word):
#     text = text.split(" ")
#     # print(text)
#     for index in text:
#         if index == banned_word:
#             # print("***")
#             index = "***"
#             return index
#         else:
#             return index
# print(index)




# censored_word("this is good", "good")r

# def clean_and_verify_logs(raw_logs):
#     chronological_logs = raw_logs[::-1]
#     chronological_logs.remove(999)
#     vip_access = chronological_logs[::2]
#     return chronological_logs, vip_access


# system_logs = [105, 104, 103, 999, 102, 101]

# clean_data, vips = clean_and_verify_logs(system_logs)

# # print("Original Logs Untouched?:", system_logs ==)
# print("Cleaned Chronological:  ", clean_data) 
# print("VIP Access Slots:       ", vips)   

raw_celcius = [5, -2, 12, 0, -8, 3, -15]
list_raw_celcius =[(numbers * 9/5) + 32 for numbers in raw_celcius if  numbers <= 0]
freezing_fahreheint = list_raw_celcius

print(f"Freezing Temps in Fahrenheint: {freezing_fahreheint}")
