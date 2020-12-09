# used stackoverflow to learn binary to string conversion in python with padding 0s
# https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros-in-python
# used stackoverflow to write to csv files as a string
#https://stackoverflow.com/questions/9157314/how-do-i-write-data-into-csv-format-as-string-not-file
#used kite to learn how to parse csv files as a string instead of object using splitlines
#https://kite.com/python/answers/how-to-parse-a-csv-string-in-python
import csv
from io import StringIO
class MyObj:
    def __init__(self, csv_string):
        self.csv_string = csv_string
    def get_map(self, column, value):
        list_csv = list(csv.reader(self.csv_string.splitlines()))
        result_string = ""
        index = list_csv[0].index(column)
        for i in range(1,len(list_csv)):
            if list_csv[i][index] == value:
                result_string = result_string + "1"
            else:
                result_string = result_string + "0"
        
        return result_string
    def matching_rows(self,dictionary):
        list_of_bitstrings = []
        for key,value in dictionary.items():
            list_of_bitstrings.append(self.get_map(key,value))
        intersection_bitstring = list_of_bitstrings[0]
        padding = len(intersection_bitstring)
        for bitstring in list_of_bitstrings:
            #print(bitstring)
            intersection_bitstring = bin(int(intersection_bitstring, 2) & int(bitstring, 2))[2:]
        return intersection_bitstring.zfill(padding)
    def get_matching_rows(self, dictionary):
        intersection_bitstring = self.matching_rows(dictionary)
        list_csv = list(csv.reader(self.csv_string.splitlines()))
        result_rows = []
        result_rows.append(list_csv[0])
        for i in range(len(intersection_bitstring)):
            if intersection_bitstring[i] == '1':
                result_rows.append(list_csv[i+1])
        
        csv_out = StringIO()
        writer = csv.writer(csv_out, delimiter=',')
        writer.writerows(result_rows)
        return csv_out.getvalue()
        
            
def bitmap(csv_string):
    return MyObj(csv_string)