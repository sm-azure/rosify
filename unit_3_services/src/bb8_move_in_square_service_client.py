#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

print ('In client')
rospy.init_node('bb8_move_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square')
execBB8 = rospy.ServiceProxy('/move_bb8_in_square', Empty)
request = Empty()
result = execBB8()

print result

#rospy.spin()

