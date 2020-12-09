class FunctionalDependency:
    def __init__(self, left_attributes_set, right_attributes_set):
        self.left_attributes_set = left_attributes_set
        self.right_attributes_set = right_attributes_set

    def __str__(self):
        return f"FunctionalDependency({self.left_attributes_set}, {self.right_attributes_set})"
    __repr__ = __str__
    
def check_funtional_dependency(list_of_dict_rows, functional_dependency):
    check = []
    res = []
    length_left = len(functional_dependency.left_attributes_set)
    col_num = len(list_of_dict_rows)
    for i in range(col_num):
        check.append([])
        res.append([])
    for i in range(col_num):
         for left_at in functional_dependency.left_attributes_set:
             check[i].append(list_of_dict_rows[i][left_at])
         for right_at in functional_dependency.right_attributes_set:
             res[i].append(list_of_dict_rows[i][right_at])
    #print(check)
    #print(res)
    for i in range(len(check)):
        starting_check = check[i]
        starting_res = res[i]
        for j in range(len(check)):
            if j != i:
                if check[j] == starting_check: #we have matching rows
                    if res[j] != starting_res: #if there is ever a mismatch
                        return False
                        
    return True