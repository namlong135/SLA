import csv
from itertools import zip_longest

# m and n are the SLA assessment threshhold
m = 100
n = 95
above_counter = 0
within_counter = 0
below_counter = 0
INITIAL_REPUTATION = 3
MIN_REPUTATION = 1
MAX_REPUTATION = 5
POINT_ELIGIBILITY = 4
ABOVE = "above"
WITHIN = "within"
BELOW = "below"
list_of_average = []
list_of_percentage = []
list_of_reputation = []

MOCK_DATA = [0.22, 0.31, 0.27, 0.25, 0.24, 0.27, 0.32, 0.35, 0.24, 0.25]

# Calculate the average response time of the service
# This function takes a list of response time as an argument
# Parameter type: list


def cal_avg(data_list):
    sum = 0
    for item in data_list:
        sum += float(item)
    avg = round(sum / len(data_list), 2)
    return avg

# Calculate the percentage of the difference between the expected response time and the measured response time
# This function takes a list of response time and a SLA time as an argument
# Parameter type: list, float


def calculate_res_time_percentage(measured_res_time, expected_res_time):
    percentage_result = []
    for i in range(len(measured_res_time)):
        sla_percentage = (float(expected_res_time) /
                          float(measured_res_time[i])) * 100
        percentage_result.append(sla_percentage)
    return percentage_result

# Assess the percentage according to the thresholds
# This function takes a percentage as an argument
# Parameter type: float


def assess_percentage(percentage):
    if (percentage >= m):
        return "above"
    elif (percentage > n and percentage < m):
        return "within"
    elif (percentage <= n):
        return "below"

# From line 49 to 100, these functions handle the reputation value of each service
# They also keep count of the number of times the service is above, within, or below the SLA threshold


def process_above_threshold(reputation):
    # global above_counter
    global above_counter

    if (reputation < MAX_REPUTATION - 1):
        reputation = reputation + 1
    elif (reputation == MAX_REPUTATION - 1 and above_counter < POINT_ELIGIBILITY):
        above_counter = increment_counter(above_counter)
    elif (reputation == MAX_REPUTATION - 1 and above_counter == POINT_ELIGIBILITY):
        above_counter = reset_counter(above_counter)
        reputation = MAX_REPUTATION

    return reputation


def process_within_threshold(reputation):
    # global within_counter
    # if (within_counter < POINT_ELIGIBILITY):
    #     within_counter = increment_counter(within_counter)
    # elif (within_counter == POINT_ELIGIBILITY):
    #     within_counter = 0
    #     reputation = reputation - 1
    reset_counter(above_counter)
    reset_counter(below_counter)
    return reputation


def process_below_threshold(reputation):
    global below_counter
    if (reputation > MIN_REPUTATION):
        reputation = reputation - 1
    elif (reputation == MIN_REPUTATION and below_counter < POINT_ELIGIBILITY):
        below_counter = increment_counter(below_counter)
    elif (reputation == MIN_REPUTATION and below_counter == POINT_ELIGIBILITY):
        reset_counter(below_counter)
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

# Remove invalid value in the row
# If there's negative value within the row, remove it


def remove_negative_value_in_row(row):
    for i in range(len(row)):
        if (i < len(row) and float(row[i]) <= 0):
            del row[i]
    return row

# Currently, this purpose of this function is to create a record of reputation value for each row


def write_to_csv(csv_file, data):
    header = []

    def get_header():
        # for i in range(len(max(data, key=len))):
        for i in range(len(data)):
            header.append("service " + str(i+1))
        return header
    file = open(csv_file, 'w', newline='')
    with file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(get_header())
        # Write the data
        writer.writerows(zip_longest(*data))


# In case you want to skip the row(s) of the csv file, specify the number of rows you want to skip
# Will not work if we not using python 'csv' module
def skip_rows(csv_file, skip):
    for i in range(skip):
        next(csv_file)

# This is the main function where the program starts
# This function will call the other functions to calculate the average
# response time, the percentage of the difference between the expected
# response time and the measured response time, and the reputation of the service

# However, this function reads the data from a csv file which isn't dynamic.
# So if there is a new csv file format, the program will not be able to read it.


def main():
    with open('./temp/transposed_data.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        # Loop through each row in the csv file
        for row in spamreader:
            formatted_row = remove_negative_value_in_row(row)
            # Assume initial reputation of all service is 1
            current_reputation = INITIAL_REPUTATION
            # Calculate the average response time of the service and store all the average in a list
            temp_avg = cal_avg(formatted_row)
            list_of_average.append(temp_avg)
            # Calculate the percentage of the difference between the expected response time and the measured response time
            temp_percentage = calculate_res_time_percentage(
                formatted_row, temp_avg)
            list_of_percentage.append(temp_percentage)
            temp_row_reputation = []

            for item in temp_percentage:
                percentageAssessment = assess_percentage(item)
                if (current_reputation == 0):
                    temp_row_reputation.append(0)
                elif (percentageAssessment == "above"):
                    current_reputation = process_above_threshold(
                        current_reputation)
                    temp_row_reputation.append(current_reputation)
                elif (percentageAssessment == "within"):
                    current_reputation = process_within_threshold(
                        current_reputation)
                    temp_row_reputation.append(current_reputation)
                elif (percentageAssessment == "below"):
                    current_reputation = process_below_threshold(
                        current_reputation)
                    temp_row_reputation.append(current_reputation)
            list_of_reputation.append(temp_row_reputation)
        write_to_csv("reputation_record.csv", list_of_reputation)
        write_to_csv("average_record.csv", [list_of_average])


main()
