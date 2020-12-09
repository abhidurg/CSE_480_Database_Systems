def censor(censored_string):
    ban_list = ["UMich", "Maize", "Blue", "Wolverines"]
    for ban_word in ban_list:
        if ban_word in censored_string:
            censored_string = censored_string.replace(ban_word, len(ban_word)*'*')
    return censored_string

class BanCount:
    def __init__(self):
        self.ban_count = 0
    def step(self, value):
        if "*" in censor(value):
            self.ban_count += 1
    def finalize(self):
        return self.ban_count
def add_aggregate_function(conn):
  conn.create_aggregate("lines_censored", 1, BanCount)