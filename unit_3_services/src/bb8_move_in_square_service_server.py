#! /usr/bin/env python

import rospy
from move_bb8 import MoveBB8
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.


def my_callback(request):
    print "move_bb8_in_square has been called"
    moveBB =  MoveBB8('/cmd_vel')
    moveBB.moveSquare()
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('move_bb8_in_square_srv') 
my_service = rospy.Service('/move_bb8_in_square', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # mantain the service open.