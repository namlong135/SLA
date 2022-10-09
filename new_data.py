# import pandas with shortcut 'pd'
# import pandas as pd
import csv

# m and n are the SLA assessment threshhold
m = 100
n = 95
above_counter = 0
within_counter = 0
below_counter = 0
MIN_REPUTATION = 1
MAX_REPUTATION = 5
# INITIAL_REPUTATION = 1

MOCK_DATA = [0.22, 0.31, 0.27, 0.25, 0.24, 0.27, 0.32, 0.35, 0.24, 0.25]

def get_current_reputation(row):
    print(row)

# def get_sla_time():


def calc_res_time(row, index, indexRange):
    current_reputation = int(row[0])
    sla_time = round(float(row[2]), 2)
    # Calculate reputation of the entire table
    if (index is None and indexRange is None):

        for cell in range(3, len(row)):

            # The difference between expected response time and measured response time in percentage
            sla_percentage = (sla_time / round(float(row[cell]), 2)) * 100

            # Above threshold
            if (sla_percentage >= m):
                current_reputation = process_above_threshold(
                    current_reputation)

            # Within threshold
            elif (sla_percentage > n and sla_percentage < m):
                current_reputation = process_within_threshold(
                    current_reputation)

            # Below threshold
            elif (sla_percentage <= n):
                current_reputation = process_below_threshold(
                    current_reputation) 

    # Calculate reputation of a single row with a specific index
    elif (index is not None and indexRange is None):
        sla_percentage = (sla_time / round(float(row[index]), 2)) * 100

        # Above threshold
        if (sla_percentage >= m):
            current_reputation = process_above_threshold(current_reputation)

        # Within threshold
        elif (sla_percentage > n and sla_percentage < m):
            current_reputation = process_within_threshold(current_reputation)

        # Below threshold
        elif (sla_percentage <= n):
            current_reputation = process_below_threshold(current_reputation)

    # Calculate reputation of a range of rows
    elif (indexRange is not None and index is None):
        for cell in range(indexRange[0], indexRange[1]):
            sla_percentage = (sla_time / round(float(row[cell]), 2)) * 100

            # Above threshold
            if (sla_percentage >= m):
                current_reputation = process_above_threshold(
                    current_reputation)

            # Within threshold
            elif (sla_percentage > n and sla_percentage < m):
                current_reputation = process_within_threshold(
                    current_reputation)

            # Below threshold
            elif (sla_percentage <= n):
                current_reputation = process_below_threshold(
                    current_reputation)

    return current_reputation


def process_above_threshold(reputation):
    # global above_counter
    global above_counter

    if (reputation < MAX_REPUTATION - 1):
        reputation = reputation + 1
    elif (reputation == MAX_REPUTATION - 1 and above_counter < 4):
        above_counter = increment_counter(above_counter)
    elif (reputation == MAX_REPUTATION - 1 and above_counter == 4):
        above_counter = reset_counter(above_counter)
        reputation = MAX_REPUTATION

    return reputation


def process_within_threshold(reputation):
    global within_counter
    if (within_counter < 4):
        within_counter = increment_counter(within_counter)
    elif (within_counter == 4):
        within_counter = 0
        reputation = reputation - 1

    return reputation


def process_below_threshold(reputation):
    global below_counter
    if (reputation > MIN_REPUTATION):
        reputation = reputation - 1
    elif (reputation == MIN_REPUTATION and below_counter < 4):
        below_counter = increment_counter(below_counter)
    elif (reputation == MIN_REPUTATION and below_counter == 4):
        reputation = 0

    return reputation


def reset_counter(counter):
    counter = 0
    return counter


def increment_counter(counter):
    counter = counter + 1
    return counter


def decrement_counter(counter):
    counter = counter - 1
    return counter


def skip_rows(csv_file, skip):
    for i in range(skip):
        next(csv_file)


def write_to_csv(csv_file, data):
    with open(csv_file, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(data)

# return the average of a tuple

def assess_percentage(percentage):
    if(percentage >= m):
        return "above"
    elif(percentage > n and percentage < m):
        return "within"
    elif(percentage <= n):
        return "below"

def cal_avg(data_list):
    average = round(sum(data_list) / len(data_list), 2)
    return average

# Calculate the percentage of the differnce between the expected response time and the measured response time
# expected_res_time = float
# measured_res_time = []
def calculate_res_time_percentage(measured_res_time, expected_res_time):
    # calculate the percentage of the difference between the expected response time and the measured response time
    percentage_result = []
    for i in range(len(measured_res_time)):
        sla_percentage = (expected_res_time / measured_res_time[i]) * 100
        percentage_result.append(sla_percentage)
    return percentage_result

# These functions below will need to be changed if different csv files are used

# Read the given csv file and write the calculated average res time to another file called "average.csv"
def get_average(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        skip_rows(spamreader, 1)
        # read to columns
        data = list(zip(*[map(float, row) for row in spamreader]))
        average_list = [cal_avg(column) for column in data]
        print(average_list)
        # write_to_csv("average.csv", average_list)
        
# Read the given csv file and format it to a usable format

# def format_input_csv_file(csv_file_path):
#     # Read_csv function which is used to read the required CSV file
#     data = pd.read_csv(csv_file_path)
#     # drop function which is used in removing columns from the CSV files
#     data.drop(data.columns[0], axis=1, inplace=True)
#     # write_to_csv("formatted_csv_file.csv", data)
#     data.to_csv("formatted_csv_file.csv", sep=',', index=False)


# print(cal_avg(MOCK_DATA))
# print(calculate_res_time_percentage(MOCK_DATA, 0.27))
# test = format_input_csv_file("Book1.csv")

# Calculate the average response time of a column and write it to a csv file called "average_sla_res_time.csv"
# write_to_csv("average_sla_res_time.csv",
#              average_column("formatted_csv_file.csv"))

# with open('formatted_csv_file.csv', 'r') as csvfile:
#     spamreader = csv.reader(csvfile)
#     skip_rows(spamreader, 1)
#     for row in spamreader:
#         get_current_reputation(row)
# print(calc_res_time(
#     row,
#     index=None,
#     indexRange=None
# ))
