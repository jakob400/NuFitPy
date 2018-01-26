import os

def list_files():
    for i in range(len(os.listdir("Data"))):
        os.listdir("Data")[i]
