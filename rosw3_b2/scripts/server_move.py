#!/usr/bin/python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from rosw3_b2.srv import move, moveResponse
import math

goal_x = 0.0
goal_y = 0.0
goal_reached = False

def pose_callback(pose):
    global goal_x, goal_y, goal_reached
    cmd_vel = Twist()

    distance = math.sqrt((goal_x - pose.x)**2 + (goal_y - pose.y)**2)

    if distance < 0.1:
        goal_reached = True
        cmd_vel.linear.x = 0
        cmd_vel.angular.z = 0
    else:
        goal_reached = False
        cmd_vel.linear.x = 1.5 * distance
        cmd_vel.angular.z = 4 * (math.atan2(goal_y - pose.y, goal_x - pose.x) - pose.theta)

    pub.publish(cmd_vel)

def handle_move_to_goal(req):
    global goal_x, goal_y, goal_reached
    goal_x = req.x
    goal_y = req.y
    goal_reached = False

    while not goal_reached:
        rospy.sleep(0.1)

    return moveResponse(success=True)

if __name__ == "__main__":
    rospy.init_node('move_to_goal_server')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    s = rospy.Service('move_to_goal', move, handle_move_to_goal)
    rospy.loginfo("Move to goal service is ready.")
    rospy.spin()