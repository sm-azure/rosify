#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ReadLaserData(object):
    def __init__(self):
        self.topic = '/kobuki/laser/scan'
        self.sub = rospy.Subscriber(self.topic, LaserScan, self.callback)
        self.laser_data = LaserScan()        
    
    def callback(self, msg):
        self.laser_data = msg
        #rospy.loginfo(self.laser_data)
    
    def getLaserData(self):
        return self.laser_data

class MoveKobuki(object):
    def __init__(self):
        self.twist = Twist()
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.angular_velocity = 0.0
        self.linear_velocity = 0.0
    
    def update_movement(self, angular_velocity, linear_velocity):
        self.linear_velocity = linear_velocity
        self.angular_velocity = angular_velocity
        self.twist.linear.x = linear_velocity
        self.twist.linear.y = 0.0
        self.twist.linear.z = 0.0
        
        self.twist.angular.x = 0.0
        self.twist.angular.y = 0.0
        self.twist.angular.z = angular_velocity
        self.pub.publish(self.twist)
    

if __name__ == "__main__":
    rospy.init_node('topics_quiz_node')
    moveKobuki = MoveKobuki()
    sensor_laser = ReadLaserData()
    
    rate = rospy.Rate(2)
    
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        global ctrl_c
        print "shutdown time!"
        moveKobuki.update_movement(0.0, 0.0)  
        ctrl_c = True
    
    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c: 
      data = sensor_laser.getLaserData()
      ranges = list(data.ranges)
      rospy.loginfo(len(ranges))
      #rospy.loginfo(data.range_min)
      #rospy.loginfo(data.range_max)
      if(len(ranges) !=0):
          center_range = ranges[len(ranges)//2]
          rospy.loginfo(center_range)
          if(center_range < 1.0):
              moveKobuki.update_movement(0.5, 0.1)
      rate.sleep()
        
