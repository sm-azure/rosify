#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):
    rospy.loginfo(msg.data)

rospy.init_node('sub')
rate = rospy.Rate(2)
pub = rospy.Subscriber('counter', Int32, callback)

rospy.spin()