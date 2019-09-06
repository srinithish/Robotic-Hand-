

## to be run on python2


import sys
sys.path.insert(0, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib")

sys.path.insert(1, "./LeapDeveloperKit_3.2.1_win/LeapDeveloperKit_3.2.1+45911_win/LeapSDK/lib/x64" )
import Leap

Leap = Leap


import time





import numpy as np


class LeapData():
    
    
    def __init__(self):
        
        self._controller = Leap.Controller()        
        self._isConnected = self._controller.is_connected
        self.finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

        
    
    
    def on_init(self, _controller):
        print ("Initialized")

    def checkConnection(self):
        return self._isConnected
    
    def getFingerTipAttributes(self,origHand,fingerName):
        
        
        ### wuold need abstipPos and relativeTipDirection
        hand_x_basis = origHand.basis.x_basis
        hand_y_basis = origHand.basis.y_basis
        hand_z_basis = origHand.basis.z_basis
        hand_origin = origHand.palm_position
        
        hand_transform = Leap.Matrix(hand_x_basis, hand_y_basis, hand_z_basis, hand_origin)
        hand_transform = hand_transform.rigid_inverse()
        
        
        absTipPosition,relativeTipDirection = None,None
        
        
        
        for finger in origHand.fingers:
            

            
            if fingerName == self.finger_names[finger.type]:
            
                fingtip_transformed_position = hand_transform.transform_point(finger.stabilized_tip_position)
                fingtip_transformed_direction = hand_transform.transform_direction(finger.direction)
                
                absTipPosition = finger.stabilized_tip_position #[x,y,z]
                absTipDirection = finger.direction #[pitch,yaw,roll]
                
                relativeTipPosition = fingtip_transformed_position 
                relativeTipDirection = fingtip_transformed_direction
                
                
                
                relativeTipDirection = np.array(relativeTipDirection)*Leap.RAD_TO_DEG        
        
        return absTipPosition,relativeTipDirection
            
        
        
        
        
    def isPointingPosture(self,hand):
        
        ###index finger open and all other fingers have to be closed
        
        
        pass
    
    
    
    def getRequiredData(self):
        
        frame = self._controller.frame()
        
        hands  = frame.hands
        
        if len(hands) > 0:
            for hand in hands: ## if there are hands present
                
                if not hand.is_left:
                    absTipPosition,relativeTipDirection = self.getFingerTipAttributes(hand,'Index')
                    print " absTipPosition:  %s,relativeTipDirection: %s" % (absTipPosition, relativeTipDirection)
                else: 
                    print 'no right hand detected'
        else:
            
            print 'no hands detected'
    
    
if __name__ == '__main__':
    
    newLeap = LeapData()
    
    while True:
        
        time.sleep(1)
        hands = newLeap.getRequiredData()
#        print(here[0].fingers[1])
        
