'''This program carries out ping tests on all the ip addresses within a .csv file.'''
# +========================================================================================================+
# |Created  |   20 June 2019    |   Author  |   PhillipG6                                                  |
# |--------------------------------------------------------------------------------------------------------|
# |Edits            |   Date    | Editor                                                                   |
# |--------------------------------------------------------------------------------------------------------|
# |                 |           |                                                                          |
# +--------------------------------------------------------------------------------------------------------+

import time
import mysql.connector
import subprocess
import os
import csv


def ping_ips(ip):
    try:
        os.system('ping -n 1 {}'.format(ip))  # Carries out the ping test then returns ping result
        time.sleep(1)
    except:
        print("The device is not running.")


list_of_ips = []
start = time.time()
open_csv = open('StoredFiles.csv', 'r')
csv_reader = csv.reader(open_csv, delimiter=',')  # Reads the values from the csv file
for row in csv_reader:
    list_of_ips.extend(row)  # Inserts the row values from the csv file into the list_of_ips list.

for ip in list_of_ips:
    ping_ips(ip)  # Calls the ping_ips list using the values from the above mentioned list as the parameters

open_csv.close()

end = time.time()
print("It took the program", end - start, "seconds to finish.")  # Prints time to completion of entire program.




