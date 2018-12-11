#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

class SpheroIMUTopic(object):
    def __init__(self):
        self.topic = '/sphero/imu/data3'
        self.sub = rospy.Subscriber(self.topic, Imu, self.callback)
        self._imu_data = Imu()
    
    def callback(self, msg):
        self._imu_data = msg
        rospy.logdebug(self._imu_data)
    
    def getIMUReading(self):
        return self._imu_data
        
if __name__ == "__main__":
    rospy.init_node('imu_topic_subscriber', log_level=rospy.INFO)
    sphero_imu = SpheroIMUTopic()
    rospy.loginfo(sphero_imu.getIMUReading())
    
    rate = rospy.Rate(0.5)
    
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        global ctrl_c
        print "shutdown time!"
        ctrl_c = True

    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        data = sphero_imu.getIMUReading()
        rospy.loginfo(data)
        rate.sleep()
    
    
        
        