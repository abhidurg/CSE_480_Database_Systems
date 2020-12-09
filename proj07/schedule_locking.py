class LegalityOfScheduleViolation(Exception): pass
class TwoPhasedLockingViolation(Exception): pass
class ConsistencyOfTransactionViolation(Exception): pass

# Do not modify code above this line

def validate_locking_schedule(actions):
    dict_of_objects = {}
    for action in actions:
        if action.object_ not in dict_of_objects:
            dict_of_objects[action.object_] = [None, None] #1st is lock state, 2nd is what transaction holds lock
    for action in actions:
        if action.type_ == "LOCK":
            if dict_of_objects[action.object_][0] == None: #its okay, there is no current lock
                dict_of_objects[action.object_][0] = "LOCKED"
                dict_of_objects[action.object_][1] = action.transaction
            else: #woops its already locked!
                if action.transaction != dict_of_objects[action.object_][1]:
                    raise LegalityOfScheduleViolation
        if action.type_ == "UNLOCK":
            dict_of_objects[action.object_][0] = None
            dict_of_objects[action.object_][1] = None
    unlock_started = [False, []] #list of all transactions that started unlocking
    for action in actions:
        print(unlock_started)
        if action.type_ == "UNLOCK":
            unlock_started[0] = True
            unlock_started[1].append(action.transaction)
        if action.type_ == "LOCK" and unlock_started[0] == True and action.transaction in unlock_started[1]:
            raise TwoPhasedLockingViolation
    dict_of_objects = {}
    for action in actions:
        if action.object_ not in dict_of_objects:
            dict_of_objects[action.object_] = [None, None] #1st is lock state, 2nd is what transaction holds lock
    for action in actions:
         if action.type_ == "LOCK":
             dict_of_objects[action.object_][0] = "LOCKED"
             dict_of_objects[action.object_][1] = action.transaction
         if action.type_ == "UNLOCK":
             dict_of_objects[action.object_][0] = None
             dict_of_objects[action.object_][1] = None
         if action.type_ == "READ" or action.type_ == "WRITE":
             if dict_of_objects[action.object_][0] != "LOCKED":
                 raise ConsistencyOfTransactionViolation
             else:
                 if dict_of_objects[action.object_][1] != action.transaction:
                    raise ConsistencyOfTransactionViolation
    for value in dict_of_objects.values():
        if value[0] == "LOCKED":
            raise ConsistencyOfTransactionViolation