import os
import time

def file_checker(file_path):
    while(True):
        files = os.listdir(file_path)
        if(len(files) > 0):
            for file_name in files:
                file_reader(file_path + file_name)
        else:   
            time.sleep(5) # sleep for 5 seconds before checking for files


def file_reader(file_name):
    output = ""
    with open(file_name) as my_file:
        for line in my_file:
            if(len(output) < 20):
                output += line[:20-len(output)]
        process_results(output)

    os.remove(file_name)


def process_results(data):
    print("sending data for storage: \n" + data)


file_checker("C:/users/emaina/OneDrive - Microsoft/Desktop/test/sample/")