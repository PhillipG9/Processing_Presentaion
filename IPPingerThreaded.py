'''This program creates threads which carry out ping tests on all the ip addresses within a .csv file.'''
# +========================================================================================================+
# |Created  |   20 June 2019    |   Author  |   PhillipG6                                                  |
# |--------------------------------------------------------------------------------------------------------|
# |Edits            |   Date    | Editor                                                                   |
# |--------------------------------------------------------------------------------------------------------|
# |                 |           |                                                                          |
# +--------------------------------------------------------------------------------------------------------+


from threading import Thread
import time
import mysql.connector
import subprocess
import os
import csv


def ping_ips(ip):
    try:
        os.system('ping -n 1 {}'.format(ip))  # Carries out ping test and returns ping result
        time.sleep(1)
    except:
        print("The device is not running.")


if __name__ == "__main__":
    list_of_ips = []
    list_of_threads = []  # Values created in each thread are stored here
    start = time.time()
    open_csv = open('StoredFiles.csv', 'r')
    csv_reader = csv.reader(open_csv, delimiter=',')  # Reads the values from the csv file
    for row in csv_reader:
        list_of_ips.extend(row)  # Inserts the values from the csv file into the list_of_ips list

    for ip in list_of_ips:
        threads = Thread(target=ping_ips, args=(ip, ))  # This creates the threads
        list_of_threads.append(threads)  # Appends the thread values to the list_of_threads list
        threads.start()  # This initialises the threads

    for item in list_of_threads:
        item.join()  # Stops the program from continuing past this point till all the threads have finished

    open_csv.close()

    end = time.time()
    print("It took the program", end - start, "seconds to finish.")  # Returns the length of time the program
    # took to finish running
