#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from sensor_msgs.msg import LaserScan

class obstacleKhoj:
    def __init__(self) -> None:
        rospy.init_node('obstacle_identifier',anonymous=True)
        self.pub = rospy.Publisher('/obstacle',String,queue_size=1)
        rospy.Subscriber('/scan',LaserScan,self.clbk)

    def clbk(self,scans):
        min_range = min(scans.ranges)
        if min_range<3.00:
            self.pub.publish('Obstacle found!')
        else:
            self.pub.publish('Everything is okay!')


if __name__=='__main__':
    node = obstacleKhoj()
    rospy.spin()
