from plot import plot
from list_files import list_files
import os
from pprint import pprint
import numpy as np
import csv

i=0
if (i == 0):
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(' ===========================================')
    print('|-|   NuFitPy: Version 3.2                |-|')
    print('|-|   Author: J Weirathmueller            |-|')
    print('|-|   Last Updated: November 20th, 2017   |-|')
    print(' ===========================================')
    print('\n\n')
    i = i+1

print("Files in Data Folder:")
print("---------------------\n")
while True:
    while True:
        while True:
            pprint(os.listdir("Data"))
            filename = input(' \nWhich of the above files would you like to analyze?\n')
            filename = "Data/" + filename
            if os.path.exists(filename):
                body, filetype = os.path.splitext(filename)
                if ( filetype == '.csv' or filetype == '.tsv' or filetype == '.dat'):
                    plot(filetype, filename)
                    response = input('\n\n\nWould you like to continue? (y/n) \n')
                    if response == 'n':
                        quit()
                else:
                    print('\nInvalid extension. \n')
            else:
                print('\nFile does not exist.\n')
