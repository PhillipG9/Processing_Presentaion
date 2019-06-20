import os
import time


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
        print(f"{file_name_to_del}.txt has been deleted")
    else:
        print(f"The file {file_name_to_del}.txt does not exist")


list_of_files = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test10", "test11"]

start = time.time()

for item in list_of_files:
    create_files(item)

time.sleep(10)

for files in list_of_files:
    del_files(files)

end = time.time()
time_taken = end - start
print("It took the program", time_taken, "seconds to finish")
