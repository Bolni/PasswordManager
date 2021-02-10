#https://pyshark.com/encrypt-and-decrypt-files-using-python/
#https://cryptography.io/en/latest/fernet.html

import json
import sys
import csv

#def readData(username, password):
    
print("Enter the website name: ")
with open('password.csv', mode='w', newline = '') as csvfile:
    fieldnames = ['website_name' , 'username' , 'password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for line in sys.stdin:
        w_name = input()
        #if(w_name == website name found in csv):
            #print("Website already saved")
            #break
        #else:
        print("Enter your username: ")
        for line in sys.stdin:
            username = input()
        print("Enter your password: ")
        for line in sys.stdin:
            password = input()