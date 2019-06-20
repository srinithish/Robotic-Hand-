# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:44:03 2019

@author: nithish k
"""

import socket
import sys
import pickle
import LeapBroadcast
#sys.path.insert(0, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib")
#
#sys.path.insert(1, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib/x64" )
#import Leap
#
#Leap = Leap
#
#
import time

#host = 'localhost'

#host  = '10.99.62.18'


host = socket.gethostbyname( '0.0.0.0' )
port = 8220


address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.gethostname()
server_socket.bind(address)
server_socket.listen(5)

print("Listening for client . . .")
conn, address = server_socket.accept()
print ("Connected to client at ", address)
#pick a large output buffer size because i dont necessarily know how big the incoming packet is   

newLeap = LeapBroadcast.LeapData()
                                                 
while True:
#    msgRecieved = conn.recv(2048);
#    print(msgRecieved)
#    msgRecieved = pickle.loads(msgRecieved)
    hands = newLeap.getRequiredData()
    
#    
#    if msgRecieved.strip() == "disconnect":
#        
#        conn.send(pickle.dumps("ack"))
#        conn.close()
#        
#        sys.exit("Received disconnect message.  Shutting down.")
#        
#    else :
        ##keep sending data     
    
    conn.sendall(pickle.dumps(hands))
    
    time.sleep(0.05)
#    conn.sendall(b'')
#        while msgRecieved != "ack":
#             print ("waiting for ack")
    
    
    
    