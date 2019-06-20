# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:14:56 2019

@author: GELab
"""


import socket
import time
import pickle
from LeapClassPy3 import CoOrdinates,LeapFinger3,LeapHand3



class MySocket(object):


    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def sendAll(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while True:
            chunk = self.sock.recv(8192)
            if chunk == b'': ##recieved empty
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
