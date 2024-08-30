#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from nav_msgs.msg import Odometry
from time import perf_counter as counter

tic,toc=0,0

class turtleKhoj:
    def __init__(self) -> None:
        rospy.init_node('position_turtle',anonymous=True)
        self.pub = rospy.Publisher('/turtle_pos_xy',String, queue_size=1)
        self.tic,self.toc=0,0
        rospy.Subscriber('/odom',Odometry,callback=self.clbk)

    def clbk(self,position):
        self.tic=counter()
        if (self.tic-self.toc)>5.00:
            pos=position.pose.pose.position
            str=f'Current Position - x: {pos.x:.2f}, y:{pos.y:.2f}'
            self.toc=self.tic
            self.pub.publish(str)



if __name__=="__main__":
    node = turtleKhoj()
    rospy.spin()
    
