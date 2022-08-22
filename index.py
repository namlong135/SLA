import csv

# m and n are the SLA assessment threshhold
m = 100
n = 95


class EFN_Reputation:

    def calc_res_time(self, sla_time, res_time):
        sla_percentage = (sla_time / res_time) * 100
        if (sla_percentage >= m):
            return 1
        elif (sla_percentage > n and sla_percentage < m):
            return 0
        elif (sla_percentage <= n):
            return -1


efn_instance = EFN_Reputation()

with open('sample.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    next(spamreader)
    for row in spamreader:
        sla_time = float(row[2])
        res_time = float(row[3])
        print(efn_instance.calc_res_time(sla_time, res_time))
