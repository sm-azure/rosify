#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('pub')
rate = rospy.Rate(2)
pub = rospy.Publisher('counter', Int32, queue_size=1)
count = 0

while not rospy.is_shutdown():
    pub.publish(count)
    count = count+ 1
    rate.sleep()
    