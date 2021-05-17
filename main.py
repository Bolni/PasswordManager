#https://pyshark.com/encrypt-and-decrypt-files-using-python/
#https://cryptography.io/en/latest/fernet.html

import json
import sys
import csv
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
    
print("Enter the website name: ")
with open('password.csv', "rb", mode='w', newline = '') as csvfile:
    
    fieldnames = ['website_name' , 'username' , 'password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    for line in sys.stdin:
        w_name = input()
        writer.writerow([w_name])
        
        print("Enter your username: ")
        for line in sys.stdin:
            username = input()
            writer.writerow(username)
        
        print("Enter your password: ")
        for line in sys.stdin:
            password = input()
            writer.writerow(password)