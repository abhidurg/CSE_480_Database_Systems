from datetime import datetime


class Server:
    def __init__(self):
        self.diction = {}
    def update_dict(self, new_dict):
        self.diction= dict(new_dict)
        #print("updated dict, now it is: ", self.diction)
        
        
        
