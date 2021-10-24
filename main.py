#https://pyshark.com/encrypt-and-decrypt-files-using-python/
#https://cryptography.io/en/latest/fernet.html

import json
import sys
import csv
import getpass
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()

    with open("key.key" , "wb") as key_file:
        key_file.write(key)

def read_key():
    return open ("key.key" , "rb").read()

def encrypt():
    f = Fernet(key)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

#def readData(username, password):

print("\nPress 1 if you want to check the saved passwords or press 2 to add a new one\n")
menu_input = int(input())

if (menu_input == 1):
    with open('password.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

elif (menu_input == 2):
    
    with open('password.csv', mode='a+', newline='') as csvfile:

        writer = csv.writer(csvfile)
        
        for i in enumerate(csvfile):
            if (i != 0):
                writer.writerow(["Website name", "Username", "Password"])
                
        website_name = input("Enter the website name: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        writer.writerow([website_name,username,password])