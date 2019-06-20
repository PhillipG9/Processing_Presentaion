"""""Volatile program that if too many threads are created with in a process the entire device will freeze
and cpu will over flow and nothing can be done"""

from multiprocessing import Process
from threading import Thread
import time


def threadedObject(thnum, pronum):
    print("This is thread", thnum, "of process", pronum)
    print("the sum of the thread number and process number is", thnum + pronum)


def createThreads(pro_num):  # Method to create threads
    th_list = []
    for i in range(1, 10):  # Limit this as using too many threads will kill your machine
        thread = Thread(target=threadedObject, args=(i, pro_num))  # Creates threads
        th_list.append(thread)  # Appends the threads to the empty list
        thread.start()

    for th in th_list:
        th.join()


if __name__ == "__main__":
    pro_list = []
    start = time.time()
    for p in range(1, 100000):  # Can have as many processes as you want
        process = Process(target=createThreads, args=(p, ))  # Creates my processes
        pro_list.append(process)
        process.start()

    for pro in pro_list:
        pro.join()

    end = time.time()

    print("It took", end - start, "seconds to run")
