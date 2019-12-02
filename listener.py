import os
import sys
import time

my_id = "0"
my_args = []


def listen():
    while True:
        print("Checking for args file...")
        for file in os.listdir("C:\\Users\\Public\\sharing\\"):
            if "args0.csv" in file:
                print("LETS GOOOOOOOOOOOO!!!!")
                with open("C:\\Users\\Public\\sharing\\args0.csv", 'r') as f:
                    for line in f.readlines():
                        my_args.append(line.split(','))
                    f.close()
                print(len(my_args))
                if len(my_args) > 0:
                    print("kicking off")
                    kickoff()
                os.rename("C:\\Users\\Public\\sharing\\args0.csv", "C:\\Users\\Public\\backups\\args0.csv")
        time.sleep(5)

def kickoff():
    print(my_args)

    for line in my_args:
        ticker = line[0]
        start = line[1]
        end = line[2]
        filename = line[3]
        price = line[4]
        bid = line[5]
        ask = line[6]
        volume = line[7]
        interest = line[8].replace('\\', '').replace('n', '')

        print("performing system call")
        os.system(
            "C:\\Users\\JoshLaptop\\source\\repos\\DRKproject\\Debug\\EveryTrade.exe " + ticker + " " + start + " " + end + " " + filename)

        # TODO: CODE TO WAIT FOR C++ SEARCHING TO COMPLETE GOES HERE

        print("removing file")
        #os.remove(filename)
        os.remove("C:\\Users\\Public\\backups\\args0.csv")
        # rinse repeat until local tape file directory is empty

    # send the output files from the search back to Dr. K machine
    # sendBackFiles()

'''
def sendBackFiles():
    for csv in os.listdir("C:\\Users\\Node0\\outputCSVfiles"):
        os.rename("C:\\Users\\Public\\outputCSVfiles\\" + csv, "\\\\MSI\\csvFiles\\" + csv)

    print("all csv output files have been moved to Dr. K's machine")
'''

listen()