from itertools import combinations
def detect_conflict(action_a, action_b):
  if action_a.transaction == action_b.transaction:
    return True
  elif action_a.object_ != action_b.object_:
    return False
  elif action_a.is_write == False and action_b.is_write == False:
    return False
  else:
    return True
def determine_precedence(list_of_actions):
    precedence_list = []
    com = combinations(list_of_actions, 2)
    for pair in list(com):
        if detect_conflict(pair[0], pair[1]) == True:
            if pair[0].transaction != pair[1].transaction:
                precedence = (pair[0].transaction, pair[1].transaction)
                precedence_list.append(precedence)
    return sorted(list(set(precedence_list)))
