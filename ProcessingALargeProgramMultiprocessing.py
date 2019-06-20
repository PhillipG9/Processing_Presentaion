from multiprocessing import Process, current_process
import time
import mysql.connector


def say_hello(num):
    print("This is process", num)
    print("This is done in parallel")


def say_goodbye(num):  # Method to say goodbye
    print("The process is almost over, let us celebrate its life.")
    print("Process", num, "has officially ended.")


if __name__ == "__main__":
    say_hello_list = []  # Empty list to store data from the hello function
    say_goodbye_list = []  # Empty list to store data from the goodbye function

    hi = 1
    start = time.time()
    for hi in range(1, 1000):  # States how many processes there will be
        process1 = Process(target=say_hello, args=(hi, ))  # Creates the processes that call the hello function
        say_hello_list.append(process1)  # Appends the process data to the empty hello list
        process1.start()  # Initiates the processes

    gi = 1
    for gi in range(1, 1000):
        process2 = Process(target=say_goodbye, args=(gi,))  # Creates second set of processes
        say_hello_list.append(process2)
        process2.start()

    for hellos in say_hello_list:  # For each item in the list stop the program from continuing till all processes
        # have been initiated
        hellos.join()

    for goodbyes in say_goodbye_list:
        goodbyes.join()

    end = time.time()  # Stores end time of program

    print("It took the program", end - start, "seconds to finish")  # Prints out time taken to complete program


