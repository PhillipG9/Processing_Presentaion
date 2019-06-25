from threading import Thread
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
        print(ping_ip)
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time_objct = datetime.fromtimestamp(timestamp)
        date_time_objct = date_time_objct.strftime("%d %b %Y %H:%M:%S.%f")[:-1]
        if ping_ip == 1:
            print(f"Cannot connect to {ip} DateStamp =", date_time_objct)
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
            print(f"Can connect to {ip} DateStamp =", date_time_objct)
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
    list_of_ips = []
    list_of_threads = []  # Values created in each thread are stored here
    open_csv = open('StoredIPs.csv', 'r')
    csv_reader = csv.reader(open_csv, delimiter=',')  # Reads the values from the csv file
    for row in csv_reader:
        list_of_ips.extend(row)  # Inserts the values from the csv file into the list_of_ips list
    open_csv.close()
    while True:
        start = time.time()
        for ip in list_of_ips:
            threads = Thread(target=ping_ips, args=(ip, ))  # This creates the threads
            list_of_threads.append(threads)  # Appends the thread values to the list_of_threads list
            threads.start()  # This initialises the threads

        for item in list_of_threads:
            item.join()  # Stops the program from continuing past this point till all the threads have finished

        end = time.time()
        time_taken = end - start
        print("It took the program", end - start, "seconds to finish.")  # Returns the length of time the program
        # took to finish running
        time.sleep(3)
