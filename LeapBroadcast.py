# -*- coding: utf-8 -*-


## to be run on python2



"""
Created on Tue Jun 18 08:52:37 2019

@author: GELab
"""

################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################
import sys
sys.path.insert(0, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib")

sys.path.insert(1, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib/x64" )
import Leap

Leap = Leap


import time



from LeapClassPy3 import CoOrdinates,LeapFinger3,LeapHand3

    


class LeapData():
    
    
    def __init__(self):
        
        self._controller = Leap.Controller()        
        self._isConnected = self._controller.is_connected
        
        
    
    
    def on_init(self, _controller):
        print ("Initialized")

    def checkConnection(self):
        return self._isConnected
    
    
    def getRequiredData(self):
        
        frame = self._controller.frame()
        
        hands = []
        
        
        for hand in frame.hands:
            
            hands.append(LeapHand3(hand))
            
            
        return hands
            
        
        
        
    
### test code
        
    
if __name__ == '__main__':
    
    newLeap = LeapData()
    
    while True:
        
        time.sleep(1)
        hands = newLeap.getRequiredData()
#        print(here[0].fingers[1])
        print(len(pickle.dumps(hands)))
