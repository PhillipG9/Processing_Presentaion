import time
import mysql.connector


def say_hello(num):
    print("This is process", num)
    print("This is done sequentially")


def say_goodbye(num):  # Method to say goodbye
    print("The process is almost over, let us celebrate its life.")
    print("Process", num, "has officially ended.")


if __name__ == "__main__":
    start = time.time()
    for i in range(1, 100000):
        say_hello(i)

    for i2 in range(1, 100000):
        say_goodbye(i2)
    end = time.time()

    print("It took the program", end - start, "seconds to finish")  # Prints out time taken to complete program
