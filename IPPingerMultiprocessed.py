'''This program creates multiple processes which carry out ping tests on all the ip addresses within a .csv file.'''
# +========================================================================================================+
# |Created  |   20 June 2019    |   Author  |   PhillipG6                                                  |
# |========================================================================================================|
# |Edits                |   Date        | Editor                                                           |
# |--------------------------------------------------------------------------------------------------------|
# |Changed Except clause| 20 June 2019  | PhillipG9                                                        |
# |--------------------------------------------------------------------------------------------------------|
# |Added timestamp      | 21 June 2019  | PhillipG9                                                        |
# |--------------------------------------------------------------------------------------------------------|
# |Changed from os.system to subprocess.call | 21 June 2019  | PhillipG9                                   |
# |--------------------------------------------------------------------------------------------------------|
# |Changed from os.system to subprocess.call | 21 June 2019  | PhillipG9                                   |
# +========================================================================================================+


from multiprocessing import Process
import time
import mysql.connector
from datetime import datetime
import csv
import subprocess


def ping_ips(ip):
    try:
        conn = mysql.connector.connect(user='root', host='localhost', password='Gocows89#', port='3307',
                                       database='ip_connections')

        cursor = conn.cursor()
        ping_ip = subprocess.call([f'ping', '-n',  '1', ip], stdout=subprocess.PIPE)  # universal_newlines=True)
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time_objct = datetime.fromtimestamp(timestamp)
        date_time_objct = date_time_objct.strftime("%d %b %Y %H:%M:%S.%f")[:-1]
        if ping_ip == 1:
            # print(f"Cannot connect to {ip} DateStamp =", date_time_objct)
            return_timestamp = date_time_objct
            return_status = "Down"
            ac = 0
            inst_data = f"""INSERT INTO connection_data(ID, IP, connection_status, date_stamp) VALUES({ac}, '{ip}', 
            '{return_status}', '{return_timestamp}')"""
            cursor.execute(inst_data)
            conn.commit()
            cursor.close()
            conn.close()
        else:
            # print(f"Can connect to {ip} DateStamp =", date_time_objct)
            return_timestamp = date_time_objct
            return_status = "Up"
            ac = 0
            inst_data = f"""INSERT INTO connection_data(ID, IP, connection_status, date_stamp) VALUES({ac}, '{ip}', 
            '{return_status}', '{return_timestamp}')"""
            cursor.execute(inst_data)
            conn.commit()
            cursor.close()
            conn.close()
    except Exception as e:
        print("There is an issue.")
        print(e)


if __name__ == "__main__":
    while True:
        list_of_ips = []
        list_of_processes = []  # Values created in each process are stored here
        open_csv = open('StoredIPs.csv', 'r')
        csv_reader = csv.reader(open_csv, delimiter=',')  # Reads the values from the csv file
        for row in csv_reader:
            list_of_ips.extend(row)  # Inserts the values from the csv file into the list_of_ips list
        open_csv.close()
        start = time.time()
        for ip in list_of_ips:
            process = Process(target=ping_ips, args=(ip, ))  # This creates the processes
            list_of_processes.append(process)  # Appends the process values to the list_of_processes list
            process.start()  # This initialises the processes

        for item in list_of_processes:
            item.join()  # Stops the program from continuing past this point till all the processes have finished

        end = time.time()
        time_taken = end - start
        print("It took the program", end - start, "seconds to ping all ips.")  # Returns the length of time the program
        # took to finish running
        list_of_ips.clear()
        time.sleep(10)



