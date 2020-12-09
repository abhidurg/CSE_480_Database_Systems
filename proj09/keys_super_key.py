class FunctionalDependency:
    def __init__(self, left_attributes_set, right_attributes_set):
        self.left_attributes_set = left_attributes_set
        self.right_attributes_set = right_attributes_set

    def __str__(self):
        return f"FunctionalDependency({self.left_attributes_set}, {self.right_attributes_set})"
    __repr__ = __str__

#used GeeksforGeeks to learn sets and how to iterate through subsets of them
#https://www.geeksforgeeks.org/python-check-if-one-list-is-subset-of-other/
#also used itertool combinations that we learned from previous homeworks
import itertools

def is_key(all_attributes, list_of_fds, attribute_set):
    s =  is_superkey(all_attributes, list_of_fds, attribute_set)
    if  not s:
        return False
    else:
        #print(len(attribute_set))
        for i in range(1,len(attribute_set)):
            #print(i)
            list_of_subsets  = list(map(set, itertools.combinations(attribute_set, i)))
            for subset in list_of_subsets:
                #print(subset)
                if  is_superkey(all_attributes, list_of_fds, subset):
                    #print(subset, "is a superkey also")
                    return False
        return True
    


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
               else:
                    if(set([att]).issubset(fd.left_attributes_set)): #if not equal, but rather a subset
                        if fd.left_attributes_set.issubset(set(res)): #if left attributes are a subset of result, we know the info
                            res = res + list(fd.right_attributes_set)
                            check = check + list(fd.right_attributes_set)
                            
           #finished checking every dependency for this attr
           if att in check:
               check.remove(att)
  if set(res) == all_attributes:
      return True
  else:
      return False