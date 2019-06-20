import time
import mysql.connector


def connect(db):  # Function that has a single parameter
    try:
        conn = mysql.connector.connect(user='root', host='localhost', password='', port='', database=dbs)
        cursor = conn.cursor()
        print("You successfully connected to", db)
        time.sleep(1)
        cursor.close()
        conn.close()
        print("You have been disconnected from", db)
    except:
        print(db, "does not exist.")
        print("\nPlease create the database")


start = time.time()

x = [i for i in range(1, 22)]

for num in x:
    dbs = f'test{num}'
    connect(dbs)
end = time.time()
time_taken = end - start

print("It took the program", time_taken, "seconds to finish running")
