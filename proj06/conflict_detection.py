def detect_conflict(action_a, action_b):
  if action_a.transaction == action_b.transaction:
    return True
  elif action_a.object_ != action_b.object_:
    return False
  elif action_a.is_write == False and action_b.is_write == False:
    return False
  else:
    return True