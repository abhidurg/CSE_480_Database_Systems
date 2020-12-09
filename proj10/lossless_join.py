class FunctionalDependency:
    def __init__(self, left_attributes_set, right_attributes_set):
        self.left_attributes_set = left_attributes_set
        self.right_attributes_set = right_attributes_set

    def __str__(self):
        return f"FunctionalDependency({self.left_attributes_set}, {self.right_attributes_set})"
    __repr__ = __str__

#used my own code from last homework to see if the intersection is a superkey for each subrelation
def is_superkey(all_attributes, list_of_fds, attribute_set):
  #first lets find a way to determine if something is a superkey
  check = []
  res = []
  check = check + list(attribute_set)
  res = res + list(attribute_set)#set of all attributes to check
  #print(check)
  while check: #while check is not empty
      for att in check:
           for fd in list_of_fds:
               if [att] == list(fd.left_attributes_set):
                   res = res + list(fd.right_attributes_set)
                   check = check + list(fd.right_attributes_set)
           #finished checking every dependency for this attr
           if att in check:
               check.remove(att)
  print(set(res))
  #if set(res) == all_attributes:
   #   return True
  #else:
   #   return False
  if all_attributes.issubset(set(res)):
      return True
  else:
      return False

def is_lossless_join(relation_set, list_of_fds, sub_relation_1, sub_relation_2):
    #check if the union is the whole set
    total = sub_relation_1.union(sub_relation_2)
    if total != relation_set:
        return False
    else:
        inter = sub_relation_1.intersection(sub_relation_2)
        res1 = is_superkey(sub_relation_1, list_of_fds, inter)
        res2 = is_superkey(sub_relation_2, list_of_fds, inter)
        if res1 or res2:
            return True
        else:
            False