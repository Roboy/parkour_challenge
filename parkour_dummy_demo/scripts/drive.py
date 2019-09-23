#!/usr/bin/env python

import rospy
from gazebo_msgs.srv import ApplyJointEffortRequest, ApplyJointEffort

rospy.init_node("simple_demo")
apply_joint_effort_srv = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
req = ApplyJointEffortRequest()
req.effort = 5.0
req.duration.secs = 30
joints = [ 'right_rear', 'left_rear']

for j in joints:
    req.joint_name = j
    apply_joint_effort_srv(req)
