from datetime import datetime
import copy

server_list = []
class Client:
    def __init__(self, server):
        self.acting_server = server
        #if self.diction not in server_list:
         #   server_list.append(self.diction)
        if server not in server_list:
            server_list.append(server)
    def put(self, key, value):
        self.acting_server.diction[key] = [value, datetime.now()]
        print("After putting ", key, " : ", value)
        for server in server_list:
            print(server.diction)
        print("\n")
    def get(self, key):
        #print("getting key: ", key)
        #print("finding key, here is dictionary: ", self.acting_server.diction)
        if key in self.acting_server.diction:
            #print("value is", self.diction[key][0])
            return self.acting_server.diction[key][0]
        else:
            return None
    def sync_servers(self):
        #for server in server_list:
         #   print(server.diction)
        base_server_dict = copy.deepcopy(server_list[0].diction)
        for server in server_list[1:]:
            for key,value  in server.diction.items():
                base_server_dict[key] = value
        #print(base_server_dict)
        for server in server_list:
            server.update_dict(base_server_dict)
        #for server in server_list:
        #    print(server.diction)
        #for server in server_list:
            #print(server, "\n")