# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:41:48 2019

@author: nithish k
"""

import socket
import time
import pickle
from LeapClassPy3 import CoOrdinates,LeapFinger3,LeapHand3

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8220))


#client_socket.setblocking(0)


numExceptions  = 0

while numExceptions<100:
    
    try:
        dataRecived = client_socket.recv(10000)
        
        dataRecived = pickle.loads(dataRecived)
        
        client_socket.send('ack')
        print(dataRecived)
        if not dataRecived :
            
            print('no data recieved')
        
        
    except Exception as e:
        numExceptions +=1
        print('Exception occured : ',e)
        time.sleep(0.1)
        pass
#    client_socket.send(pickle.dumps('ack'))
    
#send disconnect message                                                                                                                           
dmsg = "disconnect"
print ("Disconnecting")
client_socket.send(pickle.dumps(dmsg))

client_socket.close()