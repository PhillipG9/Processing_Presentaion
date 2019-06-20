# from Connections import Functions  # Imports my Connections module that I created
from threading import Thread
import time
import mysql.connector


def connect(num):  # Function that has a single parameter
    try:
        dbs = f'test{num}'
        conn = mysql.connector.connect(user='root', host='localhost', password='', port='', database=dbs)
        cursor = conn.cursor()
        print("You successfully connected to", dbs)
        time.sleep(1)
        cursor.close()
        conn.close()
        print("You have been disconnected from", dbs)
    except:
        dbs = f'test{num}'
        print(dbs, "does not exist.")
        print("\nPlease create the database")


conn_list = []  # Empty list to be appended to
x = [i for i in range(1, 22)]


  # Test data for test

start = time.time()  # Stores starting time

for num in x:
    thread = Thread(target=connect, args=(num, ))  # Creates threads
    conn_list.append(thread)  # Appends data received from the threads to the conn_list
    thread.start()  # Initiates the threads

for item in conn_list:
    item.join()  # Stops program from continuing till all threads are ready

end = time.time()  # Stores end time

print("It took", end - start, "seconds to finish")  # Prints out time taken by program to finish
