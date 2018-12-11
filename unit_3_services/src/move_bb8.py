#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class MoveBB8(object):
    def __init__(self, topic):
        self._topic = topic
        self._pub = rospy.Publisher(self._topic, Twist, queue_size=1)
        self._twist_object = Twist()
        self._rate = rospy.Rate(5)
        self._rate2 = rospy.Rate(1)
    
    def moveBB8Forward(self):
        # Forward
        self.moveBB8(0.2, 0.0)
        
    
    def moveBB8Right(self):    
        # Right
        self.moveBB8(0.0, 0.20)
        
    
    def moveSquare(self):
        for i in range(4):
            
            #Forward and Stop
            rospy.loginfo('Forward')
            self.moveBB8Forward()
            self._rate2.sleep()
            rospy.loginfo('Stop')
            self.moveBB8(0.0,0.0)
            
            #Right and Stop
            rospy.loginfo('Right')
            self.moveBB8Right()
            self._rate2.sleep()
            rospy.loginfo('Stop')
            self.moveBB8(0.0,0.0)
        
    def moveBB8(self, x, z):
        self._twist_object.linear.x = x
        self._twist_object.linear.y = 0.0
        self._twist_object.linear.z = 0.0
        
        self._twist_object.angular.x = 0.0
        self._twist_object.angular.y = 0.0
        self._twist_object.angular.z = z
        
        print(x, z)
        
        
        count = 1
        while(count <20):
            self._pub.publish(self._twist_object)
            self._rate.sleep()
            count +=1
        
            

if __name__ == "__main__":
    rospy.init_node("BB88")
    moveBB =  MoveBB8('/cmd_vel')
    rate = rospy.Rate(1)
    
    
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        global ctrl_c
        global twist_object
        global pub
        
        rospy.loginfo("shutdown time!")
        
        ctrl_c = True
        moveBB.moveBB8(0.0, 0.0)
    
    rospy.on_shutdown(shutdownhook)
    
    moveBB.moveSquare()
    
    while not ctrl_c:
         #moveBB.moveBB8(0.1, 0.5)
         rate.sleep()
    