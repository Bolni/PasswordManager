#https://pyshark.com/encrypt-and-decrypt-files-using-python/
#https://cryptography.io/en/latest/fernet.html

import json
import sys

#def readData(username, password):
    
print("Enter the website name")
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