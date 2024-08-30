#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose

commands = []

def clbk(cmnd):
    rospy.loginfo(cmnd.data)
    global commands
    commands.append(cmnd.data)


if __name__=="__main__":
    rospy.init_node('Command_history',anonymous=True)
    rospy.Subscriber('/command',String,clbk)
    rospy.spin()