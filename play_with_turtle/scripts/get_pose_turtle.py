# Viet mot node subscribe vao topic vi tri cua rua 
# In ra khoang cach Euclid cua rua den goc toa do

#!/usr/bin/python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math 

def callback(msg):
    beacon = Twist()

    if msg.x < 0.5 or msg.y < 0.5 or msg.x > 10.5 or msg.y > 10.5:
        rospy.loginfo("[GET_POSE] Turtle hit the wall")
        
        beacon.linear.x = -2
        pub.publish(beacon)
        
    rs = math.sqrt(msg.x**2 + msg.y**2)
    rospy.loginfo("[GET_POSE] Distance to turtle is: (%.2f)" % rs)

if __name__ == "__main__":
    rospy.init_node("get_pose_turtle")
    rospy.Subscriber("/turtle1/pose", Pose, callback, queue_size = 10)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
    rospy.spin()
