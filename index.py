import csv

# m and n are the SLA assessment threshhold
m = 100
n = 95
counter = 0
MIN_REPUTATION = 1
MAX_REPUTATION = 5

# class EFN_Reputation:

def calc_res_time(row):
    current_reputation = int(row[0])
    sla_time = round(float(row[2]), 2)
    for cell in range(3, len(row) - 1):
        sla_percentage = (sla_time / round(float(row[cell]), 2)) * 100    
        if (sla_percentage >= m):
            counter = 0
            if (current_reputation < MAX_REPUTATION):
                current_reputation + 1
        elif (sla_percentage > n and sla_percentage < m):
            counter = counter + 1
            if(counter < 4):
                current_reputation + 0
            else:
                counter = 0
                current_reputation - 1
        elif (sla_percentage <= n):
            counter = 0
            if( current_reputation > MIN_REPUTATION):
                current_reputation - 1
    
    return current_reputation

# def cal_reputation(self, current_rep, sla_based_point):
#     if(current_rep == 1 and sla_based_point == -1):
#         return 1
#     elif(current_rep == 5 and sla_based_point == 1):
#         return 5
#     else:
#         return current_rep + sla_based_point

# efn_instance = EFN_Reputation()
        


with open('objective_4_input.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    next(spamreader)
    for row in spamreader:
        print(calc_res_time(row))
