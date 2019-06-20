import os
import time
from threading import Thread


def create_files(file_name_to_write):
    with open(f"{file_name_to_write}.txt", "w") as f:
        f.write("This is a file and is filled with\n")
        f.write("random text that has no real meaning but it is here\n")
        f.write("anyway so please enjoy reading just before it deletes\n")
        f.write("its self during stage three of the program.\n")
        print("File created")
        time.sleep(.5)
    append_to_file(file_name_to_write)


def append_to_file(file_to_append_to):
    with open(f"{file_to_append_to}.txt", "a") as af:
        af.write("This is an appended section to the file.\n")
        af.write("This means it was not part of the initial\n")
        af.write("text written to this file.")
    read_files(file_to_append_to)


def read_files(file_name):
    with open(f"{file_name}.txt", "r") as rf:
        print(rf)
        reading = rf.read()
        print(reading)
        time.sleep(2)


def del_files(file_name_to_del):
    if os.path.exists(f"{file_name_to_del}.txt"):
        os.remove(f"{file_name_to_del}.txt")
        print(f"\n{file_name_to_del}.txt has been deleted")
    else:
        print(f"The file {file_name_to_del}.txt does not exist")


cre_files = []
del_files_list = []
list_of_files = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test10", "test11"]

start = time.time()

for item in list_of_files:
    threads = Thread(target=create_files, args=(item, ))
    cre_files.append(threads)
    threads.start()
for file in cre_files:
    file.join()

time.sleep(10)

for files in list_of_files:
    del_threads = Thread(target=del_files, args=(files,))
    del_files_list.append(del_threads)
    del_threads.start()

for delt in del_files_list:
    delt.join()

end = time.time()
time_taken = end - start
print("It took the program", time_taken, "seconds to finish")
