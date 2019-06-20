from threading import Thread
import time
import mysql.connector


def say_hello(num):  # Method to greet thread
    print("This is process", num)
    print("This is done concurrently")


def say_goodbye(num):  # Method to say goodbye
    print("The process is almost over, let us celebrate its life.")
    print("Process", num, "has officially ended.")


say_hello_list = []  # Empty list to store data from the hello function
say_goodbye_list = []  # Empty list to store data from the goodbye function

hi = 1

start = time.time()  # Stores the starting time of the program
for hi in range(1, 10000):  # States how many threads there will be
    thread1 = Thread(target=say_hello, args=(hi, ))  # Creates the threads that call the hello function
    say_hello_list.append(thread1)  # Appends the thread data to the empty hello list
    thread1.start()  # Initiates the threads

gi = 1
for gi in range(1, 10000):
    thread2 = Thread(target=say_goodbye, args=(gi,))  # Creates second set of threads
    say_hello_list.append(thread2)
    thread2.start()

for hellos in say_hello_list:  # For each item in the list stop the program from continuing till all threads have been
    # initiated
    hellos.join()

for goodbyes in say_goodbye_list:
    goodbyes.join()

end = time.time()  # Stores end time of program

print("It took the program", end - start, "seconds to finish")  # Prints out time taken to complete program
