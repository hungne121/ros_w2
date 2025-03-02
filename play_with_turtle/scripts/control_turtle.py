#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
import random

def control_turtle():
    beacon = Twist()

    beacon.linear.x = random.randrange(-2,2)
    beacon.linear.y = random.randrange(-2,2)

    beacon.angular.z = random.randrange(-3,3)
   
    return beacon

if __name__ == "__main__":
    rospy.init_node("control_turtle")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
    rate = rospy.Rate(0.5)

while not rospy.is_shutdown():
    beacon = control_turtle()
    pub.publish(beacon)
    rate.sleep()
