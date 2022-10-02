import csv

# m and n are the SLA assessment threshhold
m = 100
n = 95
above_counter = 0
within_counter = 0
below_counter = 0
MIN_REPUTATION = 1
MAX_REPUTATION = 5

# res_time_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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
                current_reputation = process_above_threshold(current_reputation)

            # Within threshold
            elif (sla_percentage > n and sla_percentage < m):
                current_reputation = process_within_threshold(current_reputation)

            # Below threshold
            elif (sla_percentage <= n):
                current_reputation = process_below_threshold(current_reputation)

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


with open('objective_4_input.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    next(spamreader)
    for row in spamreader:
        print(calc_res_time(
            row,
            index=None,
            indexRange=None
        ))
