#https://pyshark.com/encrypt-and-decrypt-files-using-python/
#https://cryptography.io/en/latest/fernet.html

import json
import sys
import csv
import pandas as pd
from cryptography.fernet import Fernet

#def readData(username, password):
    
print("Enter the website name: ")
with open('password.csv', mode='w', newline = '') as csvfile:
    
    fieldnames = ['website_name' , 'username' , 'password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    for line in sys.stdin:
        w_name = input()
        writer.writerow('website_name' : w_name)
        
        print("Enter your username: ")
        for line in sys.stdin:
            username = input()
            writer.writerow('username' : username)
        
        print("Enter your password: ")
        for line in sys.stdin:
            password = input()
            writer.writerow('password' : password)