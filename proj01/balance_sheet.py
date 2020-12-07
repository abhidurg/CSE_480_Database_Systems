import csv
from io import StringIO
def get_balances(fstring):
    string_object = StringIO(fstring) #used python docs to find info about converting string to object
    parsed_obj = csv.reader(string_object)
    parsed_string = list(parsed_obj)
    sample_dict = {}
    header = parsed_string[0]
    name_index = header.index("User")
    transaction_index = header.index("Transaction")
    amount_index = header.index("Amount")
    for i in range(1, len(parsed_string)):
        if parsed_string[i][name_index] in sample_dict:
            pass
        else:
            sample_dict[parsed_string[i][name_index]] = 0
    for i in range(1,len(parsed_string)):
        if parsed_string[i][transaction_index] == "Deposit":
            current_amount = sample_dict[parsed_string[i][name_index]]
            sample_dict[parsed_string[i][name_index]] = current_amount + int(parsed_string[i][amount_index])
        else:
            current_amount = sample_dict[parsed_string[i][name_index]]
            sample_dict[parsed_string[i][name_index]] = current_amount - int(parsed_string[i][amount_index])
    return sample_dict