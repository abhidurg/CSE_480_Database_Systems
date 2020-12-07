import operator
import copy

#used stackoverflow to learn how to use operators stored in variables:
#https://stackoverflow.com/questions/2983139/assign-operator-to-variable-in-python
#used python docs to learn how to deepcopy lists to avoid chaging the original:
#https://docs.python.org/3/library/copy.html

class Table:
    def __init__(self):
        self.list_of_dict = []
    def insert_into(self, row):
        self.list_of_dict.append(row)
    def select(self, columns_to_display):
        new_list_of_dict = copy.deepcopy(self.list_of_dict)
        for i in range(len(new_list_of_dict)):
            for column in list(new_list_of_dict[i]):
                if column not in columns_to_display:
                    del new_list_of_dict[i][column]
        return new_list_of_dict
    
    def order_by(self, columns_to_order_by):
        new_table = Table()
        new_table.list_of_dict = copy.deepcopy(self.list_of_dict)
        ordered_list_of_dict = sorted(new_table.list_of_dict, key = lambda x: [x.get(i) for i in columns_to_order_by])
        new_table.list_of_dict = ordered_list_of_dict
        return new_table
    
    def where(self, column_constraint, string_operator, literal_value):
        new_table = Table()
        new_table.list_of_dict = self.list_of_dict.copy()
        operationdict = {
        '==': operator.eq,
        '!=': operator.ne,
        '<': operator.lt,
        '<=': operator.le,
        '>': operator.gt,
        '>=': operator.ge,
        'IS': operator.is_,
        'IS NOT': operator.is_not
        }
        op = operationdict.get(string_operator)
        for row in list(new_table.list_of_dict):
            if not op(row[column_constraint], literal_value):
                new_table.list_of_dict.remove(row)
        return new_table
        
    def left_outer_join(self, right_table, left_column, right_column):
        new_table = Table()
        null_row = {}
        for column in right_table.list_of_dict[0]:
            null_row[column] = None
        for i in range(len(self.list_of_dict)):
            joined = False
            for j in range(len(right_table.list_of_dict)):
                if self.list_of_dict[i][left_column] == right_table.list_of_dict[j][right_column]:
                    if self.list_of_dict[i][left_column] != None:
                        new_dict = self.list_of_dict[i].copy()
                        new_dict.update(right_table.list_of_dict[j])
                        new_table.insert_into(new_dict)
                        joined = True
            if joined == False:
                new_dict = self.list_of_dict[i].copy()
                new_dict.update(null_row)
                new_table.insert_into(new_dict)
        return new_table