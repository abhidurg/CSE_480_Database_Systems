# Note not all or your solution should be in the function definition 

def censor(censored_string):
    ban_list = ["UMich", "Maize", "Blue", "Wolverines"]
    for ban_word in ban_list:
        if ban_word in censored_string:
            censored_string = censored_string.replace(ban_word, len(ban_word)*'*')
    return censored_string
def add_censor_function(conn):
  conn.create_function("censor", 1, censor)