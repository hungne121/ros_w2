#include "ros/ros.h"
#include "ros_w1/info.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "info_upload"); // Khoi tao node voi ten la info_upload
    ros::NodeHandle n; //  Khoi tao node handle de giao tiep voi ROS system
    ros::Publisher info_pub = n.advertise<ros_w1::info>("info", 1000); // Khoi tao publisher voi topic la info
    ros::Rate loop_rate(10); // Khoi tao rate voi toc do 10Hz

    while (ros::ok())
    {
        ros_w1::info msg; // Khoi tao message voi kieu du lieu la info

        msg.nameStudent = "Trinh Tran Phuong Tuan"; // Gan gia tri cho bien name
        msg.studentCode = 27; // Gan gia tri cho bien age
        msg.gpa = 1.0; // Gan gia tri cho bien score

        ROS_INFO("nameStudent: %s, studentCode: %d, GPA: %.2f", msg.nameStudent.c_str(), msg.studentCode, msg.gpa); // In ra
        info_pub.publish(msg); // Publish message
        ros::spinOnce(); // Xu ly cac su kien trong queue
        loop_rate.sleep(); // Sleep de dat rate
    }
    return 0;

}

