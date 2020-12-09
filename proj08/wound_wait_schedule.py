class Action:
  """
  This is the Action class.
  """
  def __init__(self, object_, transaction, type_):
    self.object_ = object_
    self.transaction = transaction
    assert type_ in ("WRITE", "COMMIT", "ROLLBACK", "LOCK", "UNLOCK", "WAIT")
    self.type_ = type_
  def __str__(self):
    return f"Action('{self.object_}', '{self.transaction}', '{self.type_}')"
  __repr__ = __str__
  def __eq__(self, other):
    return ((self.object_ == other.object_) and 
      (self.transaction == other.transaction) and 
      (self.type_ == other.type_))

# Do not modify any code above this line
#used stackoverflow to get nice one line code to check if dictionary has any non empty lists:
#https://stackoverflow.com/questions/5889611/one-liner-to-determine-if-dictionary-values-are-all-empty-lists-or-not

import copy

def wound_wait_scheduler(actions):
    transaction_dict = {}
    timestamp_dict = {}
    object_dict = {}
    return_actions = []
    Ts = 0
    for action in actions:
        if action.object_ not in object_dict:
            object_dict[action.object_] = [None, None] #lock status, and who locked it
        if action.transaction not in transaction_dict:
            transaction_dict[action.transaction] = []
            timestamp_dict[action.transaction] = Ts
            Ts += 1
    sorted_transaction_dict = dict(sorted(transaction_dict.items()))
    completed_actions_dict = copy.deepcopy(sorted_transaction_dict)
    
    while True:        
        if any(a != [] for a in sorted_transaction_dict.values()): #as long as there are actions left to do for each trans
            for key,value in sorted_transaction_dict.items():
                
                print("current action dict: ", sorted_transaction_dict)
                print("curret object dict: ", object_dict)
                print("Trying to do", key)
                print("Current value", value)
                print("completed action dict", completed_actions_dict)
                print("\n\n\n")
                if value: #list of actions for each transaction
                    for act in value: #each action is list of actions
                         if act.type_ == "COMMIT":
                             print("    Doing COMMIT", act)
                             return_actions.append(act)
                             completed_actions_dict[act.transaction].append(act) 
                             value.remove(act)
                             for obj,status in object_dict.items():
                                 if status[0] == "LOCKED" and status[1] == act.transaction:
                                     print("    Doing UNLOCK ", Action(object_=obj,transaction=act.transaction,type_="UNLOCK"))
                                     return_actions.append(Action(object_=obj,transaction=act.transaction,type_="UNLOCK"))
                                     object_dict[obj][0] = None
                                     object_dict[obj][1] = None
                             break
                         else:
                             if act.type_ == "WRITE":
                                 if object_dict[act.object_][0] == None:
                                    object_dict[act.object_][0] = "LOCKED"
                                    object_dict[act.object_][1] = act.transaction
                                    print("   Doing LOCK", Action(object_=act.object_, transaction=act.transaction, type_="LOCK"))
                                    #completed_actions_dict[act.transaction].append(Action(object_=act.object_, transaction=act.transaction, type_="LOCK"))
                                    return_actions.append(Action(object_=act.object_, transaction=act.transaction, type_="LOCK"))
                                    return_actions.append(act)
                                    print("   Doing WRITE", act)
                                    if act not in completed_actions_dict[act.transaction]:
                                        completed_actions_dict[act.transaction].append(act)
                                    value.remove(act)
                                    break
                                 else: #object already locked!
                                      if object_dict[act.object_][1] == act.transaction: #but saved, same trans!
                                          print("   Doing WRITE", act)
                                          return_actions.append(act)
                                          completed_actions_dict[act.transaction].append(act)
                                          value.remove(act)
                                          break
                                      else: #crap locks dont agree
                                          if timestamp_dict[act.transaction] > timestamp_dict[object_dict[act.object_][1]]: #act.trans is younger, make it wait
                                              print("    Doing WAIT", Action(object_="NA", transaction=act.transaction, type_="WAIT"), "beacuse ", act.transaction, " is younger")
                                              return_actions.append(Action(object_="NA", transaction=act.transaction, type_="WAIT"))
                                              break
                                          else: #act.trans older, steal lock from younger and rollback younger
                                              return_actions.append(Action(object_="NA", transaction=object_dict[act.object_][1], type_="ROLLBACK"))
                                              #value = completed_actions_dict[act.transaction] + value
                                              #sorted_transaction_dict[act.transaction] = value
                                              value_to_change = sorted_transaction_dict[object_dict[act.object_][1]]
                                              sorted_transaction_dict[object_dict[act.object_][1]] = completed_actions_dict[object_dict[act.object_][1]] + value_to_change
                                              value = sorted_transaction_dict[object_dict[act.object_][1]]
                                              sorted_transaction_dict[object_dict[act.object_][1]] = value
                                              print("    Doing ROLLBACK",  value)
                                              #need to unlock
                                              trans_to_rollback = object_dict[act.object_][1]
                                              for obj,status in object_dict.items():
                                                 print(obj, status)
                                                 if status[0] == "LOCKED" and status[1] == trans_to_rollback: #if object is locked and its locked by the younger trans
                                                     print("    Doing UNLOCK ", Action(object_=obj,transaction=trans_to_rollback,type_="UNLOCK"))
                                                     return_actions.append(Action(object_=obj,transaction=trans_to_rollback,type_="UNLOCK"))
                                                     object_dict[obj][0] = None
                                                     object_dict[obj][1] = None

                                              completed_actions_dict[object_dict[act.object_][1]] = []
                                              #finished unlocking or rollback. Give lock needed and perform next action!
                                              print("   Doing LOCK", Action(object_=act.object_, transaction=act.transaction, type_="LOCK"))
                                              return_actions.append(Action(object_=act.object_, transaction=act.transaction, type_="LOCK"))
                                              object_dict[act.object_][0] = "LOCKED"
                                              object_dict[act.object_][1] = act.transaction
                                              print("   Doing WRITE", act)
                                              return_actions.append(act)
                                              sorted_transaction_dict[object_dict[act.object_][1]].remove(act)
                                              if act not in completed_actions_dict[act.transaction]:
                                                  completed_actions_dict[act.transaction].append(act)
                                              break
                                              
                             else:
                                 return_actions.append(act)
                                 value.remove(act)
                        
        if actions:
            action_to_do = actions.pop(0)
            print("Adding", action_to_do, "to transaction list")
            sorted_transaction_dict[action_to_do.transaction].append(action_to_do)
        else:
            if any(a != [] for a in sorted_transaction_dict.values()):
                continue
            break
        
#        if any(a != [] for a in sorted_transaction_dict.values()):
#            continue
#        else:
#            action_to_do = actions.pop(0)
#            print("Adding", action_to_do, "to transaction list")
#            sorted_transaction_dict[action_to_do.transaction].append(action_to_do)
                                 
    return return_actions
