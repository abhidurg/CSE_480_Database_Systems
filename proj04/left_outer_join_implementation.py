class Table:
    def __init__(self):
        self.list_of_dict = []
    def insert_into(self, row):
        self.list_of_dict.append(row)
    def select(self, columns_to_display, columns_to_order_by):
        ordered_list_of_dict = sorted(self.list_of_dict, key = lambda x: [x.get(i) for i in columns_to_order_by])
        list_of_outputs = []
        for i in range(len(ordered_list_of_dict)):
            output = []
            for j in range(len(columns_to_display)):
                output.append(ordered_list_of_dict[i][columns_to_display[j]])
            list_of_outputs.append(output)
        return list_of_outputs
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