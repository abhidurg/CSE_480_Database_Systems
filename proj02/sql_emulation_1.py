import json
def is_it_convertible(obj):
    try:
        num = float(obj)
    except:
        return False
    else:
        return True
        
def sum_all_JSON_numbers(fstring):
    count = 0
    converted_dict = json.loads(fstring)
    values = list(converted_dict.values())
    for i in range(len(values)):
        if type(values[i]) == int:
            count += float(values[i])
        if type(values[i]) == list:
            for j in range(len(values[i])):
                convertability = is_it_convertible(values[i][j])
                if convertability:
                    count += float(values[i][j])
        if type(values[i]) == dict:
            nested_values = list(values[i].values())
            for j in range(len(values[i])):
                convertability = is_it_convertible(nested_values[j])
                if convertability:
                    count += float(nested_values[j])
    return count