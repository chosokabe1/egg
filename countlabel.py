import os 
import glob
import sys


args = sys.argv
inpath = args[1]

counter_0 = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
counter_7 = 0
counter_8 = 0
counter_9 = 0
counter_10 = 0
counter_11 = 0
counter_else = 0


files = glob.glob(inpath + "/*.txt")
for fname in files:
    with open(fname)as f:
        for line in f.readlines():
            split = line.split()
            if split[0] == '0':
                counter_0 += 1
            
            elif split[0] == '1':
                counter_1 += 1
            elif split[0] == '2':
                counter_2 += 1
            elif split[0] == '3':
                counter_3 += 1
            elif split[0] == '4':
                counter_4 += 1
            elif split[0] == '5':
                counter_5 += 1
            elif split[0] == '6':
                counter_6 += 1
            elif split[0] == '7':
                counter_7 += 1
            elif split[0] == '8':
                counter_8 += 1
            elif split[0] == '9':
                counter_9 += 1
            elif split[0] == '10':
                counter_10 += 1
            elif split[0] == '11':
                counter_11 += 1
            else:
                counter_else += 1



print("counter_0 = {}, counter_1 = {}, counter_2 = {}, counter_3 = {}, counter_4 = {}, counter_5 = {}, counter_6 = {}, counter_7 = {}, counter_8 = {}, counter_9 = {}, counter_10 = {}, counter_11 = {}, counter_else = {}".format(counter_0,counter_1,counter_2,counter_3,counter_4,counter_5,counter_6,counter_7,counter_8,counter_9,counter_10,counter_11,counter_else))