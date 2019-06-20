# from Connections import Functions  # Imports my Connections module that I created
from multiprocessing import Process
import time
import mysql.connector


def connect(num):  # Function that has a single parameter
    try:
        dbs = f'test{num}'
        conn = mysql.connector.connect(user='root', host='localhost', password='', port='', database=dbs)  # Fill in
        # port
        cursor = conn.cursor()
        print("You successfully connected to", dbs)
        time.sleep(1)
        cursor.close()
        conn.close()
        print("You have been disconnected from", dbs)
    except:
        dbs = f'test{num}'
        print("\n", dbs, "does not exist.")
        print("Please create the database\n")


if __name__ == "__main__":
    list_of_conns = []  # Create empty list
    x = [i for i in range(1, 22)]
    #  Test data for test

    start = time.time()  # stores starting time of the program
    for num in x:  # Loops through the list of databases to be tested
        process = Process(target=connect, args=(num, ))  # Creates the processes
        list_of_conns.append(process)  # Appends the processes to the empty list
        process.start()  # Initiates the process

    for item in list_of_conns:  # Loops through the database that was appended to
        item.join()  # Stops program from executing code below here till all processes are complete

    end = time.time()  # Stores ending time

    print("It took", end - start, "seconds to finish")  # prints out the time the program took to finish

