#!/usr/bin/env python3
import rospy
import sys
import termios
import tty
from geometry_msgs.msg import Twist

def get_key():
    """Hàm đọc một phím từ bàn phím, hỗ trợ phím mũi tên"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
        if key == '\x1b':  # Nếu là phím ESC (bắt đầu của phím mũi tên)
            key += sys.stdin.read(2)  # Đọc thêm 2 ký tự nữa
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def teleop():
    rospy.init_node("turtle_teleop_arrow")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    speed = 2.0  # Tốc độ di chuyển
    turn = 2.0   # Tốc độ quay

    print("Use arrow keys to move the turtle.")
    print("x to stop. q to quit.")

    while not rospy.is_shutdown():
        key = get_key()
        twist = Twist()

        if key == '\x1b[A':  # Mũi tên lên
            twist.linear.x = speed
        elif key == '\x1b[B':  # Mũi tên xuống
            twist.linear.x = -speed
        elif key == '\x1b[D':  # Mũi tên trái
            twist.angular.z = turn
        elif key == '\x1b[C':  # Mũi tên phải
            twist.angular.z = -turn
        elif key.lower() == 'x':  # Dừng ngay lập tức
            twist.linear.x = 0
            twist.angular.z = 0
        elif key.lower() == 'q':  # Thoát
            print("Thoát chương trình")
            break

        pub.publish(twist)

if __name__ == "__main__":
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass
