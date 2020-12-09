def josh_first(left, right):
    if "josh" in left and "josh" in right:
        if left == right: return 0
        if left < right: return -1
        else: return 1
    elif "josh" in left and "josh" not in right:
        return -1
    elif "josh" in right and "josh" not in left:
        return 1
    else:
        if left == right: return 0
        if left < right: return -1
        else: return 1

def add_collation(conn):
  conn.create_collation("JOSH_FIRST", josh_first)