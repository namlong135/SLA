# import pandas with shortcut 'pd'
import pandas as pd
import csv
from itertools import zip_longest

# format data from csv file
# output a file called "raw1.csv" which removed the 1 column of the origin csv file


def format_input_csv_file(csv_file_path):
    # Read_csv function which is used to read the required CSV file
    data = pd.read_csv(csv_file_path)
    # drop function which is used in removing columns from the CSV files
    data.drop(data.columns[0], axis=1, inplace=True)
    # write_to_csv("formatted_csv_file1.csv", data)
    data.to_csv("./temp/raw1.csv", sep=',', index=False, header=False)

# transpose the formatted csv file from column to row and write it to another file with the name passed in the parameter "output_file_name"
# output a file called "transposed_data.csv" which is the transpose of the "raw1" csv file


def transpose_csv_file(input_csv_file_path, output_csv_file_path):
    test = csv.reader(open(input_csv_file_path, "r"))
    a = zip_longest(*test)
    csv.writer(open(output_csv_file_path, "w")).writerows(a)


format_input_csv_file("./input/input_csv_v7.csv")
transpose_csv_file("./temp/raw1.csv", "./temp/transposed_data.csv")
