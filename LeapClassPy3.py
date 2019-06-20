# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 08:44:58 2019

@author: GELab
"""

import time

import pickle


import collections as col


import sys

if sys.version_info.major == 2:
    ##only for python2 you would need Leap
    
    sys.path.insert(0, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib")

    sys.path.insert(1, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib/x64" )
    
    import Leap





class CoOrdinates(object):
    
    
    def __init__(self,cordList,dirOrPos = 'pos'):
        
        self.x = None
        self.y = None
        self.z = None
        
        self.pitch = None
        self.yaw = None
        self.roll = None
        
        
        
        if dirOrPos == 'pos':
            self._setPositionalAttributes(cordList)
        
        if dirOrPos == 'dir':
            self._setPositionalAttributes(cordList)
            
    
    
    def _setPositionalAttributes(self,cordList, numElems = 3):
        
        
        self.x = cordList[0]
        self.y = cordList[1]
        self.z = cordList[2]
        
        return self
    
    
    def _setDirectionalAttributes(self,cordList,numElems = 3):
        
        
        self.pitch = cordList[0]
        self.yaw = cordList[1]
        self.roll = cordList[2]
        
        return self
        
        
    def __repr__(self):
        
        
        string = '(x: {}, y: {}, z: {}), (pitch: {}, roll: {}, yaw: {}) '.format(self.x,self.y,self.z ,
                                                                              self.pitch,self.yaw,self.roll
                                                                                                          )
        
        return string
        
        
    

class LeapFinger3(object):
    
    
    def __init__(self):
        
        self.type = None
        self.typeName = None
        self.relativeTipPosition = None
        self.relativeTipDirection = None
        self.absTipPosition = None
        self.absTipDirection = None
        
        
        pass
    
    
    
    
    def __repr__(self):
        
        typeName = self.typeName
        string1 = str(self.absTipPosition)
        string2 = str(self.relativeTipPosition)
        
        return  'Finger {} @ abs position is  {} \n and relative position is  {} '.format(typeName,string1,string2) 
        
    
    





class LeapHand3(object):
    
    
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    
    def __init__(self,OrigHand):
        
        
        self.fingers = []
        self.handType = None ##Left or right
        self.palmNormal = None
        self.handDirection = None
        self.palmPosition = None
        self.arm_direction = None
        self.wrist_position = None
        
        
        self.setFingerTipAttributes(OrigHand)
        self.setHandAttributes(OrigHand)
        
        
        pass
        
        
    
    
    
    
    def setFingerTipAttributes(self,origHand):
        
        hand_x_basis = origHand.basis.x_basis
        hand_y_basis = origHand.basis.y_basis
        hand_z_basis = origHand.basis.z_basis
        hand_origin = origHand.palm_position
        
        hand_transform = Leap.Matrix(hand_x_basis, hand_y_basis, hand_z_basis, hand_origin)
        hand_transform = hand_transform.rigid_inverse()
        
        
        
        for finger in origHand.fingers:
            
            newFinger = LeapFinger3()
            
            newFinger.type = finger.type
            
            newFinger.typeName = self.finger_names[finger.type]
            
            fingtip_transformed_position = hand_transform.transform_point(finger.stabilized_tip_position)
            fingtip_transformed_direction = hand_transform.transform_direction(finger.direction)
            
            newFinger.absTipPosition = CoOrdinates(finger.stabilized_tip_position,'pos')
            newFinger.absTipDirection = CoOrdinates(finger.direction,'dir')
            
            newFinger.relativeTipPosition = CoOrdinates(fingtip_transformed_position,'pos')
            newFinger.relativeTipDirection = CoOrdinates(fingtip_transformed_direction,'dir')
            
            
            
            self.fingers.append(newFinger)
        
        
        return self
        
    def setHandAttributes(self,OrigHand):
        
        
        self.handType = "Left_hand" if OrigHand.is_left else "Right_hand"
        
        
        self.palmNormal = CoOrdinates(OrigHand.palm_normal,'pos')
        self.handDirection = CoOrdinates(OrigHand.direction,'dir')
        self.palmPosition = CoOrdinates(OrigHand.palm_position, 'pos')
        self.arm_direction = CoOrdinates(OrigHand.arm.direction,'dir')
        self.wrist_position = CoOrdinates(OrigHand.arm.wrist_position,'pos')
        
        return self
    
    
    def __repr__(self):
        
        
        return 'Hand/Palm at position : {}'.format(self.palmPosition)
        
    
    
    