#include "ros/ros.h" // Thu vien ROS
#include "ros_w1/info.h" // Thu vien chua dinh nghia cua thong diep info

// Ham callback duoc goi khi nhan duoc thong diep
void infoCallback(const ros_w1::info::ConstPtr& msg)
{
    std::string nameStudent = msg->nameStudent; // Lay gia tri cua bien nameStudent
    float gpa = msg->gpa; // Lay gia tri cua bien gpa
    std::string gpaType;

    // Phan loai GPA
    if (gpa >= 3.6)
    {
        gpaType = "xuatSac";
    }
    else if (gpa >= 3.2)
    {
        gpaType = "gioi";
    }
    else if (gpa >= 2.5)
    {
        gpaType = "kha";
    }
    else
    {
        gpaType = "trungBinh";
    }
    
    // In ra thong tin nhan duoc
    ROS_INFO("%s_%s", nameStudent.c_str(), gpaType.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "info_receiver"); // Khoi tao ROS node voi ten "info_receiver"
    ros::NodeHandle n; // Tao mot NodeHandle de giao tiep voi ROS

    // Tao mot subscriber de nhan thong diep tu topic "info"
    ros::Subscriber info_sub = n.subscribe("info", 1000, infoCallback);

    ros::spin(); // Cho va xu ly cac callback

    return 0; // Tra ve 0 khi ket thuc chuong trinh
}